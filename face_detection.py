import cv2 as cv


img = cv.imread("assets/Photos/group 2.jpg")

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# blurred = cv.GaussianBlur(gray,(5,5),0)
# cv.imshow("gray img", blurred)

haarCascade = cv.CascadeClassifier("assets/models/haarcascade_frontalFace.xml")
# faces_rect = haarCascade.detectMultiScale(blurred,scaleFactor=1.1,minNeighbors=6)

# print(faces_rect)
# for (x,y,w,h) in faces_rect :
#     cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0), thickness=2)
    
# cv.imshow("img", img)

capture = cv.VideoCapture(0)

while True:
    isTrue, frame = capture.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces_rect = haarCascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=6)

    # print(faces_rect)
    for (x,y,w,h) in faces_rect :
        cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0), thickness=2)
        
    cv.imshow('Video',frame)
    
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
    
capture.release()
cv.destroyAllWindows()

cv.waitKey(0)