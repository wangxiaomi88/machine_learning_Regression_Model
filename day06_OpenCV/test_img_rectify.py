#图像矫正示例
import numpy as np
import math
import cv2

im = cv2.imread("data/paper.jpg")
# cv2.imshow("im",im)

im_gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY) #灰度化

# t, im_binary = cv2.threshold(im_gray,200,255,cv2.THRESH_BINARY) #二值化
# cv2.imshow("im_binary",im_binary) #无论怎么调阈值，效果并不好，改用其他方法
#
# #sobel边沿提取
# im_sobel = cv2.Sobel(im_gray, #原始图像
#                   cv2.CV_64F, #
#                   1, #垂直方向
#                   1, #水平方向
#                   ksize=5) #核大小
# cv2.imshow("im_sobel",im_sobel) #边沿分布太复杂，不好
#
# #laplacian边沿提取
# im_laplacian = cv2.Laplacian(im_gray, #原始图像
#                   cv2.CV_64F,) #核大小
# cv2.imshow("im_laplacian",im_laplacian) #更糟糕

#先模糊化后膨胀，把原图中细小的分支合并，方便后面边沿提取，模糊后轮廓提取时不容易中断！
im_blurred = cv2.GaussianBlur(im_gray,(5,5),0)
im_dilated = cv2.dilate(im_blurred,(3,3))
im_erode = cv2.erode(im_blurred,(3,3))
# im_edge = cv2.subtract(im_erode,im_dilated)
# cv2.imshow("im_dilated",im_dilated) #效果很不错


k = np.ones((10,10),np.uint8) #运算核
im_open = cv2.morphologyEx(im_blurred,cv2.MORPH_OPEN,k)
# cv2.imshow("im_open",im_open)

im_close = cv2.morphologyEx(im_blurred,cv2.MORPH_CLOSE,k)
cv2.imshow("im_close",im_close)



#canny边沿提取
# im_canny = cv2.Canny(im_dilated,50,240)
# cv2.imshow("im_canny_dilated",im_canny) #效果很不错
# im_canny = cv2.Canny(im_open,50,240)
# cv2.imshow("im_canny_open",im_canny) #效果很不错
im_canny = cv2.Canny(im_close,10,120)
cv2.imshow("im_canny_close",im_canny) #效果很不错




#轮廓检测
cnts,hie = cv2.findContours(im_canny.copy(), #原始图像
                            cv2.RETR_EXTERNAL, #只检测外轮廓
                            cv2.CHAIN_APPROX_SIMPLE) #只保留轮廓的终点坐标

for cnt in cnts:
    print(cnt.shape)

#绘制轮廓
im_cnt = cv2.drawContours(im.copy(),cnts,-1,(0,0,255),3)
cv2.imshow("im_cnt",im_cnt) #效果很不错


#计算轮廓面积，并排序
if len(cnts)>0:
    cnts = sorted(cnts, #需要排序的列表
                  key=cv2.contourArea, #以计算轮廓面积的函数作为排序依据
                  reverse=True) #逆序排列

    for c in cnts: #遍历排序后的每个轮廓
        peri = cv2.arcLength(c,True) #计算封闭轮廓的周长
        approx = cv2.approxPolyDP(c,0.02*peri,True) #多边形拟合
        # 拟合出来的第一个四边形，则认为是纸张的轮廓（面积足够大，又是四边形）
        if len(approx) == 4:
            docCnt = approx
            break

#绘制找到的四边形的角点
im2=im.copy()
points = []
for peak in docCnt:
    peak = peak[0]
    #绘制角点
    cv2.circle(im2,tuple(peak),10,(0,0,255),3)
    points.append(peak)
cv2.imshow("im_point",im2)


#矫正
h=np.linalg.norm(points[0]-points[1]) #两点之间的欧式距离
w=np.linalg.norm(points[0]-points[3]) #两点之间的欧式距离
print("宽、高为：",w,h)

src = np.array([points[0],points[1],points[2],points[3]],dtype="float32") #二维数组，存储了原纸张逆时针方向的4个角点
dst = np.array([[0,0],[0,h],[w,h],[w,0]],dtype="float32") #矫正的目标坐标


m = cv2.getPerspectiveTransform(src,dst) #生成透视矩阵
im_result = cv2.warpPerspective(im.copy(),m,(int(w),int(h)))
cv2.imshow("im_result",im_result)



cv2.waitKey()
cv2.destroyAllWindows()