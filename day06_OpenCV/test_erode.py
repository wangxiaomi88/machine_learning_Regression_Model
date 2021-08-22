#图像腐蚀
import numpy as np
import cv2

im = cv2.imread("data/5.png")
cv2.imshow("im",im)

#腐蚀
kernel = np.ones((3,3),np.uint8) #腐蚀核
print(kernel)
erosion = cv2.erode(im,
                    kernel,
                    iterations=12) #迭代次数
cv2.imshow("erode",erosion)


cv2.waitKey()
cv2.destroyAllWindows()
