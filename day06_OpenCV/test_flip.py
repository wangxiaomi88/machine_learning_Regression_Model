import cv2

im = cv2.imread("data/Linus.png")
cv2.imshow("im",im)

im_flip0 = cv2.flip(im,0)
cv2.imshow("imflip0",im_flip0)

im_flip1 = cv2.flip(im,1)
cv2.imshow("imflip1",im_flip1)

cv2.waitKey()
cv2.destroyAllWindows()