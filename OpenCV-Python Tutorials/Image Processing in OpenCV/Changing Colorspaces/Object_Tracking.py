import cv2 as cv
import numpy as np

cap = cv.VideoCapture(1)

while True:
    # Take each frame
    _, frame = cap.read()
    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_RGB2HSV)
    # define range of blue color in HSV
    lower_blue = np.array([115, 100, 100])
    upper_blue = np.array([125, 255, 255])
    # # Threshold the HSV image to get only blue colors
    mask = cv.inRange(hsv, lower_blue, upper_blue)
    # # Bitwise-AND mask and original image
    res = cv.bitwise_and(frame, frame, mask=mask)

    cv.imshow('frame', frame)
    cv.imshow('mask', mask)
    cv.imshow('res', res)
    k = cv.waitKey(25)
    if k == ord('q'):
        break

cv.destroyAllWindows()


