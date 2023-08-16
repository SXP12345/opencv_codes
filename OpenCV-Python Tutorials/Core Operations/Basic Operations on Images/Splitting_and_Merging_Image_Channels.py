import numpy as np
import cv2 as cv

img = cv.imread("pic.jpg")
if img is None:
    print("file could not be read")

print(img.shape)

b, g, r = cv.split(img)
img_ = cv.merge((b, g, r))
# b channel
cv.imshow("Display b channel", b)
k = cv.waitKey(0)
# g channel
cv.imshow("Display g channel", g)
k = cv.waitKey(0)
# r channel
cv.imshow("Display r channel", r)
k = cv.waitKey(0)
# merge image
cv.imshow("Display merge image", img_)
k = cv.waitKey(0)


b = img[:, :, 0]
g = img[:, :, 1]
r = img[:, :, 2]
# b channel
cv.imshow("Display b channel", b)
k = cv.waitKey(0)
# g channel
cv.imshow("Display g channel", g)
k = cv.waitKey(0)
# r channel
cv.imshow("Display r channel", r)
k = cv.waitKey(0)
# merge image
cv.imshow("Display merge image", img_)
k = cv.waitKey(0)

img_[:, :, 1] = 0
cv.imshow("Display merge image", img_)
k = cv.waitKey(0)

# cv.split()是一个代价高昂的操作（就时间而言）。因此，仅在必要时才使用它。否则，请使用 Numpy 索引。
