import numpy as np
import cv2

a = cv2.imread("data/lena.jpg",1)
b = cv2.imread("data/lily_square.png",1)

# 直接相加，越加越白
dst1 = cv2.add(a,b)
cv2.imshow("dst1",dst1)


#图像按权重相加
dst2=cv2.addWeighted(a,0.3, #图像1和权重
                     b,0.8, #图像2和权重
                     0) #亮度调节

cv2.imshow("dst2",dst2)

cv2.waitKey()
cv2.destroyAllWindows()