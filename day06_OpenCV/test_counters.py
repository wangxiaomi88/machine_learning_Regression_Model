# 查找并绘制轮廓
import numpy as np
import cv2

im = cv2.imread("data/3.png")
cv2.imshow("im", im)

# 灰度化与二值化
im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
ret, im_binary =cv2.threshold(im_gray,127,255,cv2.THRESH_BINARY)
cv2.imshow("im_binary", im_binary)


# 查找轮廓
cnts,hie = cv2.findContours(im_binary, #原图（经过二值化处理）
                                cv2.RETR_EXTERNAL, #只检测外轮廓
                                cv2.CHAIN_APPROX_NONE) #存储所有轮廓点

#findContours返回值中最重要的是cnts，改值为一个列表，其中每一个元素为一个3维的ndarray数组！
print(type(cnts))
for cnt in cnts:
    print(cnt.shape,type(cnt))

print(cnts[0])


#绘制轮廓
im_cnt = cv2.drawContours(im, #原始图像
                          cnts, #轮廓数据，findContours的返回值
                          -1, #绘制第几个轮廓，-1表示绘制所有轮廓
                          (0,0,255), #轮廓颜色
                          2) #轮廓宽度
cv2.imshow("im_cnt", im_cnt)


cv2.waitKey()
cv2.destroyAllWindows()
