import cv2
import sys

img1 = cv2.imread("assets/tennis01.jpg")
img2 = cv2.imread("assets/tennis02.jpg")
img3 = cv2.imread("assets/tennis03.jpg")

if img1 is None:
    sys.exit("Could not read the image.")

cv2.namedWindow("Display Window", cv2.WINDOW_NORMAL)
# Using resizeWindow()
cv2.resizeWindow("Display Window", 1000, 1000)

cv2.imshow("Display Window", img1)

while True:
    try:
        k = cv2.waitKey(100)
        if k == ord('a'):
            cv2.imshow("Display Window", img2)
        elif k == ord('s'):
            cv2.imshow("Display Window", img1)
        elif k == ord('d'):  
            cv2.imshow("Display Window", img3)
        elif k == 27:  #27 is the ESC key
            cv2.destroyAllWindows()
            sys.exit("done")
        else:
            continue
    except KeyboardInterrupt:
        cv2.destroyAllWindows()
        sys.exit("done")


