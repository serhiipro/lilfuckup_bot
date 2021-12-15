import cv2 as cv


photo = cv.imread("D:\lilfuckup_bot\photos\photos\file_0.jpg")

original = cv.imread(photo, cv.IMREAD_COLOR)
gray = cv.imread(photo, cv.IMREAD_GRAYSCALE)
unchange = cv.imread(photo, cv.IMREAD_UNCHANGED)

cv.imshow('Original', original)
cv.imshow('Gray', gray)
cv.imshow('Unchange', unchange)

cv.waitKey(0)
cv.destroyAllWindows()

