# 绘制轮廓外接矩形框
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

#绘制轮廓
im_cnt = cv2.drawContours(im, #原始图像
                          cnts, #轮廓数据，findContours的返回值
                          -1, #绘制第几个轮廓，-1表示绘制所有轮廓
                          (0,0,255), #轮廓颜色
                          2) #轮廓宽度
cv2.imshow("im_cnt", im_cnt)


#根据轮廓，产生外接矩形框参数
x,y,w,h = cv2.boundingRect(cnts[0])

#绘制矩形框
# brcnt = np.array( [ [x,y],[x+w,y],[x+w,y+h],[x,y+h] ] ) #二维数组也能运行？
brcnt = np.array( [ [[x,y]],[[x+w,y]],[[x+w,y+h]],[[x,y+h]] ] ) #矩形的点的顺序是有要求的，否则绘制出交叉线！
print(brcnt,type(brcnt))

im_brcnt = cv2.drawContours(im,[brcnt],-1,(0,255,255),2) #第二个参数是一个包含多条三维（或二维）数组轮廓的列表
# im_brcnt = cv2.drawContours(im_brcnt,brcnt,-1,(0,0,255),5) #剥离最外层视为列表

cv2.imshow("result", im_brcnt)


cv2.waitKey()
cv2.destroyAllWindows()
