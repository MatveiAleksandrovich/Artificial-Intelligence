import cv2

img = cv2.imread('assets/PersLogo_4.jpg', -1)
img = cv2.resize(img,  (0, 0), fx=0.5, fy=0.5)
img = cv2.rotate(img, cv2.cv2.ROTATE_90_COUNTERCLOCKWISE)

cv2.imwrite('assets/new_img.jpg', img)

cv2.imshow('Image ', img)
cv2.waitKey(0)
cv2.destroyWindow()
