import cv2 as cv
import numpy as np

img = cv.imread("pic.jpg")
cv.imshow("Display img", img)
k = cv.waitKey(0)

# Python:
# cv.resize(	src, dsize[, dst[, fx[, fy[, interpolation]]]]	) ->	dst
# (1) src	input image.
# (2) dst	output image; it has the size dsize (when it is non-zero) or the size computed from src.size(), fx, and fy; the type of dst is the same as of src.
# (3) dsize	output image size; if it equals zero (None in Python), it is computed as:
# dsize = Size(round(fx*src.cols), round(fy*src.rows))
# Either dsize or both fx and fy must be non-zero.
# (4) fx	scale factor along the horizontal axis; when it equals 0, it is computed as
# (double)dsize.width/src.cols
# (5) fy	scale factor along the vertical axis; when it equals 0, it is computed as
# (double)dsize.height/src.rows
# (6) interpolation	 interpolation method, see InterpolationFlags

res = cv.resize(img, None, fx=1.5, fy=1.5, interpolation=cv.INTER_LINEAR)
cv.imshow("Display res", res)
k = cv.waitKey(0)

height, width = img.shape[:2]
res = cv.resize(img, (2*width, 2*height), interpolation=cv.INTER_CUBIC)
cv.imshow("Display res", res)
k = cv.waitKey(0)



