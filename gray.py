import cv2
capture = cv2.VideoCapture(0)
while(True):
    ret,frame = capture.read()
    grayFrame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    cv2.imshow('video gray',grayFrame)
    cv2.imshow('video original',frame)
    cv2.imshow('video hsv',hsv)
    if cv2.waitKey(1) & 0XFF == ord('x'):
        break
capture.release()
cv.destroyAllWindows() 
