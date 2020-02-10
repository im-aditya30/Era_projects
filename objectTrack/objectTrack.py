import cv2
import numpy as np

def nothing(x):
    pass


cap = cv2.VideoCapture('Shots.mp4'); #if 0 doesn't owork use -1
ret, frame1 = cap.read()
ret, frame2 = cap.read()

while cap.isOpened():
    frame = cv2.imread('1.jpg')
    diff = cv2.absdiff(frame1,frame2)
    gray = cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),0)
    _, thresh =cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
    dilated  = cv2.dilate(thresh,None,iterations =3)
    contours, _ = cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    # cv2.drawContours(frame1, contours, -1, (0,255,0) ,)
    for contour in contours:
        (x,y,w,h) = cv2.boundingRect(contour)

        if cv2.contourArea(contour) <100:
            continue
        cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)




    cv2.imshow("feed",frame1)
    frame1 = frame2
    ret, frame2 = cap.read()

    key = cv2.waitKey(10) #& 0xFF
    if key == 27:
        break

cv2.destroyAllWindows()
cap.release()
