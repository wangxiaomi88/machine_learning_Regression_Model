import numpy as np
import cv2

#图像裁剪（利用数组切片操作实现）

#随机裁剪
def random_crop(im,w,h):
    # 随机产生裁剪的起点x，y坐标
    start_x = np.random.randint(0,im.shape[1])
    start_y = np.random.randint(0, im.shape[0])

    new_img = im[start_y:start_y+h, start_x:start_x+w] #这里不写第三维通道的 ,: 的表达，可以兼容二维矩阵的黑白图像！
    return new_img



def center_crop(im,w,h):
    # 随机产生裁剪的起点x，y坐标
    start_x = int(im.shape[1]/2 - w/2)
    start_y = int(im.shape[0]/2 - h/2)

    new_img = im[start_y:start_y+h, start_x:start_x+w] #这里不写第三维通道的 ,: 的表达，可以兼容二维矩阵的黑白图像！
    return new_img



if __name__ == '__main__':
    im = cv2.imread("data/banana_1.png",1)
    cv2.imshow("im",im)

    cropped = random_crop(im,150,150)
    cv2.imshow("random_crop",cropped)

    cropped = center_crop(im, 200, 300)
    cv2.imshow("center_crop", cropped)

    cv2.waitKey()
    cv2.destroyAllWindows()