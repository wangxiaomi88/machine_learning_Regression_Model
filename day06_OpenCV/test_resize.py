import numpy as np
import cv2

im = cv2.imread("data/Linus.png")
cv2.imshow("im",im)

h,w = im.shape[:2]

dst_size = (int(w/2), int(h/2)) # 计算缩放后的图像的宽高元组，注意与im.shape的高宽取值顺序相反！
dst_size = (int(w*2), int(h*2)) # 计算缩放后的图像的宽高元组，注意与im.shape的高宽取值顺序相反！
resized1 = cv2.resize(im,dst_size,interpolation=cv2.INTER_NEAREST)
resized2 = cv2.resize(im,dst_size,interpolation=cv2.INTER_LINEAR)



cv2.imshow("resized1",resized1)
cv2.imshow("resized2",resized2)

cv2.waitKey()
cv2.destroyAllWindows()

