#绘制轮廓的最小圆形包围圈
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

(x,y),radius = cv2.minEnclosingCircle(cnts[0]) #产生轮廓的最小外接圆形参数
print((x,y),radius)
center = (int(x),int(y))
radius = int(radius)

im_circle = cv2.circle(im,center,radius,(0,255,255),2)
cv2.imshow("im_cnt", im_circle)


cv2.waitKey()
cv2.destroyAllWindows()
