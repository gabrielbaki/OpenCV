import cv2 as cv

#Reading Images
#img = cv.imread('Photos/cat.png')

#cv.imshow('Cat', img)

#cv.waitKey(0)

#Reading Videos
capture = cv.VideoCapture('Videos/Dog.mp4') 
#For parameter 0 is webcam 1, 2, 3 are cameras connected

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame) #show frame bt frame 

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()

