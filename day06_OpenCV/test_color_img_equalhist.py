import cv2
import numpy as np
import matplotlib.pyplot as plt

im = cv2.imread("data/sunrise.jpg")
cv2.imshow("im",im)

#BGR转换为YUV
yuv = cv2.cvtColor(im,cv2.COLOR_BGR2YUV)

#绘制直方图
plt.subplot(2,1,1)
plt.hist(yuv[:,:,0].ravel(), #返回一个扁平数组
         256,[0,256],label="origin")
plt.legend()

#取出亮度通道，进行equalhist处理，并将处理结果赋值回原图像
# yuv[:,:,0] = cv2.equalizeHist(yuv[:,:,0])
yuv[...,0] = cv2.equalizeHist(yuv[...,0])

plt.subplot(2,1,2)
plt.hist(yuv[:,:,0].ravel(), #返回一个扁平数组
         256,[0,256],label="equalhist")
plt.legend()
plt.show()



#YUV转换为BGR
im_equ_y = cv2.cvtColor(yuv,cv2.COLOR_YUV2BGR)

cv2.imshow("im_equ_y",im_equ_y)





cv2.waitKey()
cv2.destroyAllWindows()