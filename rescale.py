import cv2 as cv

#Reading Images
img = cv.imread('Photos/cat.png')

#cv.imshow('Cat', img)

def rescaleFrame(frame, scale=0.75):
    #works for images, videos, and live videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width, height):
    #Live video
    capture.set(3, width)
    capture.set(4, height)

cv.imshow('Cat', rescaleFrame(img))

#Reading Videos
capture = cv.VideoCapture('Videos/Dog.mp4') 
#For parameter 0 is webcam 1, 2, 3 are cameras connected

while True:
    isTrue, frame = capture.read()

    frame_resized =  rescaleFrame(frame)

    cv.imshow('Video', frame) #show frame bt frame 
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()

