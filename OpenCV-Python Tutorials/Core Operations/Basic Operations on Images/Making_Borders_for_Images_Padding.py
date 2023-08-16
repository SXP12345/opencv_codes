import cv2 as cv

img1 = cv.imread('pic.jpg')
cv.imshow("Display img1", img1)
k = cv.waitKey(0)
# Last element is replicated throughout, like this: aaaaaa|abcdefgh|hhhhhhh
replicate = cv.copyMakeBorder(img1, 50, 50, 50, 50, cv.BORDER_REPLICATE)
cv.imshow("Display replicate", replicate)
k = cv.waitKey(0)
# Border will be mirror reflection of the border elements, like this : fedcba|abcdefgh|hgfedcb
reflect = cv.copyMakeBorder(img1, 50, 50, 50, 50, cv.BORDER_REFLECT)
cv.imshow("Display reflect", reflect)
k = cv.waitKey(0)
#  Same as above, but with a slight change, like this : gfedcb|abcdefgh|gfedcba
reflect101 = cv.copyMakeBorder(img1, 50, 50, 50, 50, cv.BORDER_REFLECT_101)
cv.imshow("Display reflect101", reflect101)
k = cv.waitKey(0)
# Can't explain, it will look like this : cdefgh|abcdefgh|abcdefg
wrap = cv.copyMakeBorder(img1, 50, 50, 50, 50, cv.BORDER_WRAP)
cv.imshow("Display wrap", wrap)
k = cv.waitKey(0)
# Adds a constant colored border. The value should be given as next argument.
constant = cv.copyMakeBorder(img1, 50, 50, 50, 50, cv.BORDER_CONSTANT, value=[0, 255, 0])
cv.imshow("Display constant", constant)
k = cv.waitKey(0)