#利用opencv实现图像读取、显示、保存

import cv2

im = cv2.imread("data/Linus.png", # 图像路径
                1) # 1为读取彩色图像，0为灰度图像

print(type(im)) #打印图像数据类型
print(im.shape) #打印图像数据形状

cv2.imshow("im",im) # 显示图像，第一个参数名称不要重复
cv2.imwrite("data/Linus_new_wj.png",im)


cv2.waitKey() #等待用户按某个键，阻塞
cv2.destroyAllWindows() #销毁所有创建的窗口


