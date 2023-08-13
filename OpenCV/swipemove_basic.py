"""
Project Hologram - Swipe Move Basic
The program plays 2 different videos (left turn and right turn) of an object based on 
user's gesture input (left swipe and right swipe)

Next steps/libraries and resources
Python front end + back end: https://streamlit.io/gallery
3D model rendering: http://www.open3d.org/
"""

import cv2
import numpy as np
import sys, time


# Video playback function
def video_playback(cap):
    cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
    while cap.isOpened():
        # Capture frame-by-frame
        ret, frame = cap.read()
        if ret == True:
            # Display the resulting frame
            cv2.imshow("Display Window", frame)
            cv2.waitKey(25)
        # Break the loop
        else:
            break


def main():
    # Load the videos & stationary image
    stationary_img = cv2.imread("assets/stationary.jpg")
    left_swipe = cv2.VideoCapture("assets/left_swipe.mp4")
    right_swipe = cv2.VideoCapture("assets/right_swipe.mp4")

    # Initialize the main display window
    cv2.namedWindow("Display Window", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Display Window", 1000, 1000)
    cv2.imshow("Display Window", stationary_img)

    # Initialize the camera and background subtraction
    gesture_cap = cv2.VideoCapture(1)  # Change to 0 if using built-in webcam
    bg_subtractor = cv2.createBackgroundSubtractorMOG2()

    # Initialize variables for hand tracking
    prev_x = 0
    direction = None

    while True:
        ret, frame = gesture_cap.read()

        if not ret:
            break

        # Apply background subtraction
        fg_mask = bg_subtractor.apply(frame)

        # Remove noise and enhance the mask
        fg_mask = cv2.erode(fg_mask, None, iterations=2)
        fg_mask = cv2.dilate(fg_mask, None, iterations=2)

        # Find contours in the mask
        contours, _ = cv2.findContours(
            fg_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
        )

        # Find the largest contour (presumably the hand)
        if contours:
            hand_contour = max(contours, key=cv2.contourArea)
            M = cv2.moments(hand_contour)
            if M["m00"] != 0:
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])

                # Determine the direction of hand swipe
                if prev_x != 0:
                    if cx - prev_x > 50:
                        direction = "Swipe Right"
                        print("Swipe Right")
                        video_playback(right_swipe)
                        # time.sleep(1)
                        continue
                    elif prev_x - cx > 50:
                        direction = "Swipe Left"
                        print("Swipe Left")
                        video_playback(left_swipe)
                        # time.sleep(1)
                        continue
                    else:
                        direction = None

                prev_x = cx
        else:
            cv2.imshow("Display Window", stationary_img)

        # Exit the loop based on conditions
        if (
            cv2.waitKey(1) & 0xFF == ord("q")
            or cv2.getWindowProperty("Display Window", 0) == -1
        ):
            break

    # Release the camera and close all windows
    gesture_cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
