import numpy as np
import cv2

im = cv2.imread("data/lena.jpg",0)
cv2.imshow("im1",im)

#锐化算子1
sharpen1_k = np.array([
    [-1,-1,-1],
    [-1,9,-1],
    [-1,-1,-1]
])
im_sharpen1 = cv2.filter2D(im,-1,sharpen1_k)
cv2.imshow("im_sharpen1",im_sharpen1)



#锐化算子2
sharpen2_k = np.array([
    [0,-1,0],
    [-1,8,-1],
    [0,1,0]
])/4
im_sharpen2 = cv2.filter2D(im,-1,sharpen2_k)
cv2.imshow("im_sharpen2",im_sharpen2)

#锐化算子3
sharpen3_k = np.array([
    [-1,-1,-1],
    [0,0,0],
    [1,1,1]
])
im_sharpen3 = cv2.filter2D(im,-1,sharpen3_k)
cv2.imshow("im_sharpen3",im_sharpen3)

cv2.waitKey()
cv2.destroyAllWindows()
