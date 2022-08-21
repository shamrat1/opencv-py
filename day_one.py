import re
from turtle import width
import cv2 as cv


#108803

def rescaleFrame(frame, scale = 0.50):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)
    
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

# img = cv.imread("assets/Photos/cat.jpg")
# cv.imshow("Cat",img)
# cv.waitKey(0)

capture = cv.VideoCapture(0)

while True:
    isTrue, frame = capture.read()
    resized = rescaleFrame(frame,2)
    cv.imshow('Video',resized)
    
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
    
capture.release()
cv.destroyAllWindows()