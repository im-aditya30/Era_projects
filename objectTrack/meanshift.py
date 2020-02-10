import numpy as np
import cv2
cap = cv2.VideoCapture('Shots.mp4')

ret, frame = cap.read()

x, y, width, height = 448, 0, 1472, 1080
track_window = (x, y, width, height)
roi = frame[y: y+ height, x : x+width]
cv2.imshow('roi', roi)
hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv_roi, np.array((0., 60., 32.)), np.array((180.,255.,255.)))
roi_hist = cv2.calcHist([hsv_roi], [0],mask, [180], [0,180])

cv2.normalize(roi_hist,roi_hist,0 ,255 ,cv2.NORM_MINMAX)
term_crit = ( cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10 ,1)

while 1:
    ret, frame = cap.read()
    if ret == 1:

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        dst = cv2.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)
        ret, track_window = cv2.CamShift(dst, track_window, term_crit)

        x, y ,w,h = track_window
        final_img = cv2.rectangle(frame, (x,y), (x+w, y+h), 255 ,3)
        cv2.imshow('dst', dst)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) == 27:
            break
    else:
        break


