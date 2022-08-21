import cv2 as cv


#108803

img = cv.imread("assets/Photos/cat.jpg")
cv.imshow("Cat",img)
cv.waitKey(0)

capture = cv.VideoCapture("assets/Videos/dog.mp4")

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video',frame)
    
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
    
capture.release()
cv.destroyAllWindows()