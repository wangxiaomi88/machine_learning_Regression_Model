import cv2
import numpy as np
import matplotlib.pyplot as plt

im = cv2.imread("data/sunrise.jpg",0)

cv2.imshow("im",im)

im_equ = cv2.equalizeHist(im)
cv2.imshow("im_equ",im_equ)


#绘制直方图
plt.subplot(2,1,1)
plt.hist(im.ravel(), #返回一个扁平数组
         256,[0,256],label="origin")
plt.legend()

plt.subplot(2,1,2)
plt.hist(im_equ.ravel(), #返回一个扁平数组
         256,[0,256],label="equalhist")
plt.legend()

plt.show()



cv2.waitKey()
cv2.destroyAllWindows()