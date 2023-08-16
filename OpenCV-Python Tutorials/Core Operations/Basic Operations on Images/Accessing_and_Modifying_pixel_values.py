import numpy as np
import cv2 as cv

img = cv.imread("pic.jpg")
if img is None:
    print("file could not be read")

px = img[100, 100]
print(px)

blue = img[100, 100, 0]
print(blue)

img[100, 100] = [255, 255, 255]
print(img[100, 100])

cv.imshow("Display window", img)
k = cv.waitKey(0)
if k == ord("s"):
    cv.imwrite("saved_by_opencv.jpg", img)

"""
上述方法通常用于选择数组的一个区域，
例如前 5 行和后 3 列。对于单个像素访问，

Numpy 数组方法 array.item() 和 array.itemset() 被认为更好。
然而，它们总是返回一个标量，
因此如果您想访问所有 B、G、R 值，
则需要为每个值单独调用 array.item() 。
"""

print(img.item(10, 10, 2))
img.itemset((10, 10, 2), 100)
print(img.item(10, 10, 2))
