import cv2

im = cv2.imread("data/lena.jpg",0)
cv2.imshow("im",im)


#二值化
t, rst = cv2.threshold(im,
                       80, #阈值
                       255, #最大值
                       cv2.THRESH_BINARY) #二值化
cv2.imshow("binary",rst)


t, rst = cv2.threshold(im,
                       80, #阈值
                       255, #最大值
                       cv2.THRESH_BINARY_INV) #反二值化
cv2.imshow("binary_inverse",rst)

cv2.waitKey()
cv2.destroyAllWindows()


