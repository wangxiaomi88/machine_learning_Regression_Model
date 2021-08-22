#图像闭运算
import numpy as np
import cv2

im1 = cv2.imread("data/lena.jpg")
im2 = cv2.imread("data/10.png")
cv2.imshow("im1",im1)
cv2.imshow("im2",im2)

#执行闭运算
k1 = np.ones((10,10),np.uint8) #闭运算核
k2 = np.ones((15,15),np.uint8) #闭运算核
r1 = cv2.morphologyEx(im1,cv2.MORPH_CLOSE,k1)
r2 = cv2.morphologyEx(im2,cv2.MORPH_CLOSE,k2)

cv2.imshow("im1_close",r1)
cv2.imshow("im2_close",r2)

cv2.waitKey()
cv2.destroyAllWindows()



