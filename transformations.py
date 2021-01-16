import cv2 as cv
import numpy as np

img = cv.imread('Photos/cat.png')

cv.imshow('Cat', img)

# Translation
def translateImg(img, x, y):
    transMatrix = np.float32([[1,0,x],[0,1,y]]) #translation matrix
    dimensions = (img.shape[1], img.shape[0]) #x & y axis
    return cv.warpAffine(img, transMatrix, dimensions)

# -x -> left
# x -> right
# -y -> up
# y -> down

translatedImage = translateImg(img, 100, 100) # shift right 100px, down 100px
cv.imshow('Translated Image', translatedImage)

def rotate(img, angle, rotPoint=None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width,height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, 45)  #rotate imgae 45 deg clockwise
cv.imshow('Rotated', rotated)

rotated_r = rotate(rotated, 45)  
cv.imshow('Rotated Rotated', rotated_r)

#resizing
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC) #read docs on interplation parameter diffeerences
cv.imshow('Resized', resized)

#Flipping
flip = cv.flip(img, 0) # 0=vertical, 1=horizontal, -1=both
cv.imshow('Flip', flip)

#Cropping
cropped = img[200:400, 300:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)