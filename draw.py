import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8') #height, width, number of color channels
cv.imshow('Blank', blank)

#paint image certain color (green)
#blank[:] = 0,255,0
#use range of pixels to draw red box in image
#blank[200:300, 300:400] = 0,0,255
#cv.imshow('Green', blank)

#draw rectangle
#cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness=2)#params: origin, end, color RGB, thickness
cv.rectangle(blank, (0,0), (blank.shape[1]//2,blank.shape[0]//2), (0,255,0), thickness=-1)
cv.imshow('Rectangle', blank)

#Draw a circle
cv.circle(blank, (blank.shape[1]//2,blank.shape[0]//2), 40, (0,0,255), thickness=3)#param 40 is radius, esle is same as prev
cv.imshow('Circle', blank)

#draw a line
cv.line(blank, (0,0), (blank.shape[1]//2,blank.shape[0]//2), (255,255,255), thickness=3)
cv.imshow('Line', blank)

#write text
cv.putText(blank, 'Hello my name is G!', (0,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (100,155,150), 2)
cv.imshow('Text', blank)

cv.waitKey(0)