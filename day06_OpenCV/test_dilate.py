#图像膨胀
import numpy as np
import cv2

im = cv2.imread("data/6.png")
cv2.imshow("im",im)

#膨胀
kernel = np.ones((3,3),np.uint8) #膨胀核
print(kernel)
dilation = cv2.dilate(im,
                    kernel,
                    iterations=5) #迭代次数
cv2.imshow("erode",dilation)


cv2.waitKey()
cv2.destroyAllWindows()
