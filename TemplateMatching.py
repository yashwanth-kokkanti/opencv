import cv2
import numpy as np

#cap = cv2.VideoCapture(0) ## 0 indicates first web cam

img_big = cv2.imread('bigImage.jpg')
img_gray = cv2.cvtColor(img_big, cv2.COLOR_BGR2GRAY)

template = cv2.imread('smallImage.jpg', 0)
w, h = template.shape[::-1]

res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)

threshold = 0.77
loc = np.where(res >= threshold)

for pt in zip(*loc[::-1]):
    cv2.rectangle(img_big, pt, (pt[0]+w, pt[1]+h), (0, 255, 255), 2)

cv2.imshow('detected', img_big)

