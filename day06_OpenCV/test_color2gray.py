import cv2

im = cv2.imread("data/Linus.png", 1) # 1为读取彩色图像，0为灰度图像
im_gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

print(im_gray.shape)

cv2.imshow("im",im) # 显示图像，第一个参数名称不要重复
cv2.imshow("im_gray",im_gray)


cv2.waitKey() #等待用户按某个键，阻塞
cv2.destroyAllWindows() #销毁所有创建的窗口


