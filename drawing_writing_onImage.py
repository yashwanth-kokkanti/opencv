import numpy as np

import cv2

img = cv2.imread('watch.jpg', cv2.IMREAD_COLOR)

cv2.line (img, (0, 0), (150, 150), (255, 0, 255), 15) # 15 is pixel

cv2.rectangle(img, (450, 350), (750, 600), (0, 255, 0), 5) # Rectangle

cv2.circle(img, (250, 150), 60, (0, 0, 255), 10) ## Circle 55 is raduis


pts = np.array([[150, 125], [200, 250], [285, 345], [95, 185], [445, 565]], np.int32)
#pts = pts.reshape((-1, 1, 2))
cv2.polylines(img, [pts], True, (0, 0, 255), 3) ## True to connect final point to last point

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'Hi Yashwanth', (285, 405), font, 1, (0, 0, 0), 2, cv2.LINE_AA)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
