import cv2 as cv

img = cv.imread('Photos/cat.png')
cv.imshow('Cats', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# pixels <150 become black, >255 become white
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('Simple Thresh', thresh)

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('Simple Thresh Inverse', thresh_inv)

# Adaptive Tresholding, decides pixel range per sub block for thresh relative to the micro sub block of the image and slides to next and so on ...
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C,
cv.THRESH_BINARY, 11, 3)
cv.imshow('Adaptive Thresh', adaptive_thresh)

cv.waitKey(0)