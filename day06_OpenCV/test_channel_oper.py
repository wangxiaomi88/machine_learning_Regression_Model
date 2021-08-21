import cv2

im = cv2.imread("data/opencv2.png")
cv2.imshow("im",im)

#取出蓝色通道，并显示（单通道图像，所以显示成灰度图像）
b = im[:,:,0] #0为第一个蓝色通道
cv2.imshow("b",b)

#抹掉蓝色通道（将蓝色通道置为0）
im[:,:,0] = 0
cv2.imshow("im-b0",im)

im[:,:,1] = 0
cv2.imshow("im-b0-g0",im)

cv2.waitKey()
cv2.destroyAllWindows()
