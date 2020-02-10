import cv2
import numpy as np
from matplotlib import pyplot as plt


def nothing(x) :
    pass


cap = cv2.VideoCapture('Shots.mp4')

# cv2.namedWindow("Tracking")
#
# cv2.createTrackbar("lT", "Tracking", 0, 255, nothing)
# cv2.createTrackbar("uT", "Tracking", 0, 255, nothing)

while 1:
    ret, frame = cap.read()
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, mask = cv2.threshold(img, 68, 255, cv2.THRESH_BINARY_INV)
    th2 = cv2.adaptiveThreshold(img, 255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 2)
    # th2 = cv2.adaptiveThreshold(img, 255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)

    kernal = np.ones((2, 3), np.uint8)
    kernel = np.ones((2, 2), np.float32)/4

    dilation = cv2.dilate(th2, kernal)
    erosion = cv2.erode(th2, kernal, iterations=1)
    opening = cv2.morphologyEx(th2, cv2.MORPH_OPEN, kernal,iterations=2)
    # closing = cv2.morphologyEx(th2, cv2.MORPH_CLOSE, kernal)
    mg = cv2.morphologyEx(th2, cv2.MORPH_TOPHAT, kernal)

    mgd = cv2.filter2D(opening, -1, kernel)
    blur = cv2.blur(opening, (2, 2))
    gblur = cv2.GaussianBlur(opening, (3, 3), 0)
    mblur = cv2.medianBlur(erosion, 3)
    bil = cv2.bilateralFilter(th2, 3, 75, 75)
    # titles = ['im', 'mask', 'dilation', 'er ', 'op', 'mgd', 'b', 'gb', 'm','bil']
    # images = [img, th2, dilation, erosion, opening, mgd, blur, gblur, mblur, bil]

    # l_t = cv2.getTrackbarPos("lT",  "Tracking")
    # u_t = cv2.getTrackbarPos("uT", "Tracking")

    canny = cv2.Canny(img, 95, 158)
    # lines = cv2.HoughLines(canny, 1, np.pi / 180, 200)
    # titles = ['img', 'ca']
    # images = [img, canny]
    # for i in range(2):
    #     plt.subplot(1,2, i+1), plt.imshow(images[i], 'gray')
    #     plt.title(titles[i])
    #     plt.xticks([]), plt.yticks([])
    #
    # plt.show()

    # for line in lines:
    #     rho, theta = line[0]
    #     a = np.cos(theta)
    #     b = np.sin(theta)
    #     x0 = a * rho
    #     y0 = b * rho
    #
    #     x1 = int(x0 + 1000 * (-b))
    #     y1 = int(y0 + 1000 * (a))
    #     x2 = int(x0 - 1000 * (-b))
    #     y2 = int(y0 - 1000 * (a))
    #     cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    cv2.imshow('img', frame)
    cv2.imshow('cn', canny)
    key = cv2.waitKey(1)  # & 0xFF
    if key == 27:
        break

cv2.destroyAllWindows()
cap.release()