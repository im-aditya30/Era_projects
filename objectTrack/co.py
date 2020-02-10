import cv2
import numpy as np
from matplotlib import pyplot as plt

# img = cv2.imread('untitled2.png')
# imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# ret, thresh = cv2.threshold(imgray, 70, 255, 0)
# contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
# print(str(len(contours)))
# print (contours[0])
#
# cv2.drawContours(img, contours, 100, (0, 255, 0), 3)
cap = cv2.VideoCapture('Shots.mp4')
img = cv2.imread('3.png')
# cv2.imshow('imag', img)
# cv2.imshow('Imagray', imgray)
titles = ['img']
images = [img]
for i in range(1):
    plt.subplot(1,1, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    # plt.xticks([]), plt.yticks([])
#
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()