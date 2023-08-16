import cv2 as cv
import numpy as np

img1 = cv.imread('pic.jpg')
cv.imshow("Display img1", img1)
k = cv.waitKey(0)

x = np.uint8([250])
y = np.uint8([10])

print(cv.add(x, y)) # 250 + 10 = 255

print(x + y) # 250 + 10 = 260 % 256 = 4
