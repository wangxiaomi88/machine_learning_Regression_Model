#透视变换
import numpy as np
import cv2

im = cv2.imread("data/pers.png")
cv2.imshow("im",im)
rows,cols = im.shape[:2]
print(rows,cols)

#制定映射坐标
pts1 = np.float32([[58,2],[8,196],[126,196],[167,9]]) #原坐标点,[[x1,y1],[x2,y2],[x3,y3],[x4,y4]]，列表内顺序无关，但pts1和pts2要对应
pts2 = np.float32([[16,2],[8,196],[169,196],[167,8]]) #目标点坐标

#生成透视变换矩阵
M = cv2.getPerspectiveTransform(pts1,pts2)


#执行变换
dst1 = cv2.warpPerspective(im, #原始图像
                     M, #变换矩阵
                     (cols,rows)) #输出图像大小
cv2.imshow("prespected",dst1)



#生成透视变换矩阵
M = cv2.getPerspectiveTransform(pts2,pts1)
#执行变换
dst2 = cv2.warpPerspective(dst1, #原始图像
                     M, #变换矩阵
                     (cols,rows)) #输出图像大小
cv2.imshow("prespected2",dst2)

cv2.waitKey()
cv2.destroyAllWindows()
