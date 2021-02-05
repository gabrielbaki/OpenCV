import cv2 as cv

#img = cv.imread('Photos/1face.jpeg')
#cv.imshow('1 Face', img)

img = cv.imread('Photos/UN.jpg')
cv.imshow('UN', img)

# get gray image bcs only need edges not color
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Face', gray)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

face_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

print(f'No. of faces found = {len(face_rect)}')

# draw rectangle around faces detected
for (x,y,w,h) in face_rect:
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)

cv.imshow('Detected Faces', img)

cv.waitKey(0)
