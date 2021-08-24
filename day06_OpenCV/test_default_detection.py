#利用图像技术实现芯片瑕疵检测
import numpy as np
import math
import cv2

im = cv2.imread("data/CPU3.png")
cv2.imshow("im",im)

im_gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY) #灰度化
cv2.imshow("im_gray",im_gray)

t, im_binary = cv2.threshold(im_gray,160,255,cv2.THRESH_BINARY) #二值化
# cv2.imshow("im_binary",im_binary)

#提取轮廓，实心化填充
cnts,hie = cv2.findContours(im_binary,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
mask = np.zeros(im_binary.shape,np.uint8) #创建全0矩阵（全黑图像），大小与原图一致
im_fill = cv2.drawContours(mask,cnts,-1,(255,0,0),-1) #绘制线粗细设为-1时表示为纯色填充
# cv2.imshow("im_fill",im_fill)

#图像减法，找出瑕疵的区域
im_sub=cv2.subtract(im_fill,im_binary)
cv2.imshow("im_sub",im_sub)


#图像的闭运算（先膨胀后腐蚀），将离散瑕疵点合并在一点
k = np.ones((10,10),np.uint8) #运算核
im_close = cv2.morphologyEx(im_sub,cv2.MORPH_CLOSE,k,iterations=3)
cv2.imshow("im_close",im_close)

#提取瑕疵区域的轮廓，绘制最小外接圆形
cnts,hie = cv2.findContours(im_close,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
cnts = sorted(cnts,key=np.shape,reverse=True)

for cnt in cnts:
    print(cnt.shape)

#产生最小外接圆数据
(x,y),radius = cv2.minEnclosingCircle(cnts[0])
center = (int(x),int(y))
radius = int(radius)
print(center,radius)
im_circle = cv2.circle(im_close,center,radius,(255,255,255),2)
cv2.imshow("im_circle",im_circle)

#在原始图像上绘制瑕疵外接圆
im_default = cv2.circle(im,center,radius,(0,0,255),2)
cv2.imshow("im_default",im_default)
# 计算外接圆形面积
area = np.pi * radius * radius
# 计算x瑕疵轮廓面积
area = cv2.contourArea(cnts[0])
print(area)
if area > 12:
    print("镀盘表面有瑕疵")


cv2.waitKey()
cv2.destroyAllWindows()