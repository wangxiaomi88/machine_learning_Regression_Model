#使用多边形对轮廓进行拟合
import numpy as np
import cv2

im = cv2.imread("data/cloud.png")
cv2.imshow("im", im)

# 灰度化与二值化
im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
ret, im_binary =cv2.threshold(im_gray,127,255,cv2.THRESH_BINARY)
cv2.imshow("im_binary", im_binary)


# 查找轮廓
cnts,hie = cv2.findContours(im_binary, #原图（经过二值化处理）
                                cv2.RETR_EXTERNAL, #只检测外轮廓
                                cv2.CHAIN_APPROX_NONE) #存储所有轮廓点



# #精度1
adp = im.copy()
epsilon = 0.005 * cv2.arcLength(cnts[0],True) #计算轮廓的周长并量化误差，TRUE表示封闭
approx1 = cv2.approxPolyDP(cnts[0],epsilon,True) #构造轮廓的拟合多边形，轮廓与多边形之间最大距离不超过epsilon，TRUE表示图形封闭
im_adp1 = cv2.drawContours(adp,[approx1],-1,(0,255,255),3)
cv2.imshow("im_adp1", im_adp1)

#精度2
adp = im.copy()
epsilon = 0.02 * cv2.arcLength(cnts[0],True) #计算轮廓的周长并量化误差，TRUE表示封闭
approx2 = cv2.approxPolyDP(cnts[0],epsilon,True) #构造轮廓的拟合多边形，轮廓与多边形之间最大距离不超过epsilon，TRUE表示图形封闭
im_adp2 = cv2.drawContours(adp,[approx2],-1,(0,255,255),3)
cv2.imshow("im_adp2", im_adp2)

cv2.waitKey()
cv2.destroyAllWindows()
