import numpy as np
import cv2

cap = cv2.VideoCapture('Shots.mp4')
fgbg = cv2.createBackgroundSubtractorKNN()
# kernal = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))

while cap.isOpened():
    kernel = np.ones((5,5), np.uint8)
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    erosion = cv2.erode(gray, kernel, iterations=1)
    canny = cv2.Canny(frame, 95, 158)
    fgmask = fgbg.apply(canny)
    # fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN,kernal)

    opening = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel, iterations=2)
    contours, _ = cv2.findContours(fgmask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    cv2.drawContours(frame, contours, -1, (0, 255, 0), 2)
    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)

        if cv2.contourArea(contour) < 100 or cv2.contourArea(contour) > 700:
            continue
        # print(contours)
        # if cv2.num
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.imshow('Frame', frame)
    cv2.imshow('Fra', fgmask)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
