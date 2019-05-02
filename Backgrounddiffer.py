import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(1):
    t0 = cap.read()[1]
    t1 = cap.read()[1]
    
    film = cv2.absdiff(t0, t1)
    cv2.imshow('video',film)
    key = cv2.waitKey(30) 
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()



