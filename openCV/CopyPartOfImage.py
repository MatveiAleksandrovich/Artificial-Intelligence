import cv2
import random

img = cv2.imread('assets/PersLogo_4.jpg', -1)

tag = img[100:1000, 500:1400]
tag = cv2.resize(img, (0, 0), fx=0.2, fy=0.2)

img[0:tag.shape[0], 0:tag.shape[1]] = tag

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
