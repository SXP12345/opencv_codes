import numpy as np
import cv2 as cv

img = cv.imread("pic.jpg")
if img is None:
    print("file could not be read")

print(img.shape)

ball = img[200:400, 500:600]
img[0:200, 0:100] = ball

cv.imshow("Display window", img)
k = cv.waitKey(0)
if k == ord("s"):
    cv.imwrite("saved_by_opencv.jpg", img)