import numpy as np
import cv2

im = cv2.imread("data/lena.jpg")
cv2.imshow("im1",im)

#中值滤波
im_median_blur = cv2.medianBlur(im,5)
cv2.imshow("im_median_blur",im_median_blur)

#均值滤波
im_mean_blur = cv2.blur(im,(7,7))
cv2.imshow("im_mean_blur",im_mean_blur)


#高斯滤波
im_gaussian_blur = cv2.GaussianBlur(im,(7,7), 0) #原始图像，高斯滤波器大小，标准差（当为0时标准差根据核尺寸自动计算，不太推荐）
cv2.imshow("im_gaussian_blur",im_gaussian_blur)


#自定义高斯核
gaussian_k = np.array([
    [1,4,7,4,1],
    [4,16,26,16,4],
    [7,26,41,26,7],
    [4,16,26,16,4],
    [1,4,7,4,1]
], np.float32) / 273
print(np.sum(gaussian_k))
#使用filter2D执行滤波计算
im_gaussian_blur2 = cv2.filter2D(im, #原始图像
                                                  -1, #图像深度，-1表示与原图相同
                                                  gaussian_k) #自定义滤波器核
cv2.imshow("im_gaussian_blur2",im_gaussian_blur2)

cv2.waitKey()
cv2.destroyAllWindows()

