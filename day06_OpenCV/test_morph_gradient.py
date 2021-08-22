#形态学梯度：膨胀图像 - 腐蚀图像
import numpy as np
import cv2

im1 = cv2.imread("data/lena.jpg")
im2 = cv2.imread("data/6.png")
cv2.imshow("im1",im1)
cv2.imshow("im2",im2)

k = np.ones((3,3),np.uint8) #开运算核
r1 = cv2.morphologyEx(im1,cv2.MORPH_GRADIENT,k)
r2 = cv2.morphologyEx(im2,cv2.MORPH_GRADIENT,k)

cv2.imshow("im1_gradient",r1)
cv2.imshow("im2_gradient",r2)

cv2.waitKey()
cv2.destroyAllWindows()
