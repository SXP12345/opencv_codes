import numpy as np
import cv2 as cv

img = cv.imread("pic.jpg")
if img is None:
    print("file could not be read")


# Image properties include number of rows, columns, and channels; type of image data; number of pixels; etc.

# The shape of an image is accessed by img.shape.
# It returns a tuple of the number of rows, columns, and channels (if the image is color):
print(img.shape)

# Total number of pixels is accessed by img.size:
print(img.size)

# Image datatype is obtained by `img.dtype`:
print(img.dtype)
