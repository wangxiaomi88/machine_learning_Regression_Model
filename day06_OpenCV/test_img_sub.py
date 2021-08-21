#图像相减
import numpy as np
import cv2

a = cv2.imread("data/3.png",1)
b = cv2.imread("data/lena.jpg",1)

h,w = a.shape[:2]
b=cv2.resize(b,(w,h),interpolation=cv2.INTER_LINEAR)


dst_ab = cv2.subtract(a,b) #图像需要尺寸相同，第一个图像各个像素灰阶值减去第二个图像对应位置的灰阶值，若小于0则记为0！
cv2.imshow("dst_ab",dst_ab)

dst_ba = cv2.subtract(b,a) #图像需要尺寸相同，第一个图像各个像素灰阶值减去第二个图像对应位置的灰阶值，若小于0则记为0！
cv2.imshow("dst_ba",dst_ba)

dst_add = cv2.add(dst_ba,dst_ab)
cv2.imshow("dst_add",dst_add)


cv2.waitKey()
cv2.destroyAllWindows()