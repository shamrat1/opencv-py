import cv2 as cv
import numpy as np

# blank image
blank = np.zeros((500,500,3),dtype='uint8')

# painting bg color
blank[:] = 255,255,255

# to paint color in certain location
# blank[200:300,10:300] = 0,255,0

# drawing a rect
cv.rectangle(blank,(50,50),(blank.shape[1] // 2,blank.shape[0] // 2),(0,255,0), thickness=2)

# drawing circle
cv.circle(blank,((blank.shape[1] // 2) + 50,(blank.shape[0] // 2) + 50),50,(0,0,255),2)

# drawing line
cv.line(blank,(5,10),(500,500),(255,0,0),thickness=5)

# writing text
cv.putText(blank,"Something major",(0,500 - 50), cv.FONT_HERSHEY_TRIPLEX,1.0,(0,0,0),1)


cv.imshow('Blank Image', blank)
cv.waitKey(0)