import cv2
import sys
import time

# Libraries
# Python front end + back end: https://streamlit.io/gallery
# 3D model rendering: http://www.open3d.org/

stationary_img = cv2.imread("assets/stationary.jpg")
left_swipe = cv2.VideoCapture("assets/left_swipe.mp4")
right_swipe = cv2.VideoCapture("assets/right_swipe.mp4")

cv2.namedWindow("Display Window", cv2.WINDOW_NORMAL)
# Using resizeWindow()
cv2.resizeWindow("Display Window", 1000, 1000)

cv2.imshow("Display Window", stationary_img)


def video_playback(cap):
    cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
    while cap.isOpened():
        # Capture frame-by-frame
        ret, frame = cap.read()
        if ret == True:
            # Display the resulting frame
            cv2.imshow("Display Window", frame)

            # Press Q on keyboard to exit
            if cv2.waitKey(25) & 0xFF == ord("q"):
                break

        # Break the loop
        else:
            break


while True:
    try:
        k = cv2.waitKey(100)

        if k == ord("a"):
            video_playback(left_swipe)
        elif k == ord("d"):
            video_playback(right_swipe)
        elif k == 27:  # 27 is the ESC key
            cv2.destroyAllWindows()
            sys.exit("done")
        else:
            continue

        cv2.imshow("Display Window", stationary_img)

    except KeyboardInterrupt:
        cv2.destroyAllWindows()
        sys.exit("done")
