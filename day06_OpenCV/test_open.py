#图像开运算
import numpy as np
import cv2

im1 = cv2.imread("data/7.png")
im2 = cv2.imread("data/8.png")
cv2.imshow("im1",im1)
cv2.imshow("im2",im2)

#执行开运算
k = np.ones((10,10),np.uint8) #开运算核
r1 = cv2.morphologyEx(im1,cv2.MORPH_OPEN,k)
r2 = cv2.morphologyEx(im2,cv2.MORPH_OPEN,k)

cv2.imshow("im1_open",r1)
cv2.imshow("im2_open",r2)

cv2.waitKey()
cv2.destroyAllWindows()



