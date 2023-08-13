import cv2
import numpy as np
import time

# Initialize the camera
cap = cv2.VideoCapture(1)

# Initialize backround subtractor
bg_subtractor = cv2.createBackgroundSubtractorMOG2()

# Initialize variables for hand tracking
prev_x = 0
direction = None

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # # Convert the frame to grayscale
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # # Apply Gaussian blur to reduce noise and improve hand detection
    # blurred = cv2.GaussianBlur(gray, (15, 15), 0)

    # # Apply thresholding to create a binary image
    # _, thresholded = cv2.threshold(blurred, 127, 255, cv2.THRESH_BINARY)

    # # Find contours in the thresholded image
    # contours, _ = cv2.findContours(
    #     thresholded.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    # )

    # Apply background subtraction
    fg_mask = bg_subtractor.apply(frame)

    # Remove noise and enhance the mask
    fg_mask = cv2.erode(fg_mask, None, iterations=2)
    fg_mask = cv2.dilate(fg_mask, None, iterations=2)

    # Find contours in the mask
    contours, _ = cv2.findContours(fg_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

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
                    time.sleep(1)
                    continue
                elif prev_x - cx > 50:
                    direction = "Swipe Left"
                    print("Swipe Left")
                    time.sleep(1)
                    continue
                else:
                    direction = None

            prev_x = cx

            # Draw the contour and direction on the frame
            cv2.drawContours(frame, [hand_contour], 0, (0, 255, 0), 2)
            cv2.putText(
                frame, direction, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2
            )

    # Display the frame
    cv2.imshow("Hand Swipe Detection", frame)

    # Exit the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()
