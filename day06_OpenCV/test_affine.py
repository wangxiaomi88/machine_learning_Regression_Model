#图像仿射变换（旋转，平移）

import numpy as np
import cv2

def translate(im,x,y):
    """
    对图像进行平移变换
    :param im: 原始图像数据
    :param x: 水平方向平移像素
    :param y: 垂直方向平移像素
    :return: 返回平移后的图像数据
    """

    h,w = im.shape[:2] #取出原图像的高度、宽度

    # 定义平移矩阵
    M = np.float32([[1,0,x],
                              [0,1,y]])


    #调用warpAffine函数实现平移变换
    shifted = cv2.warpAffine(im, #原始图像
                             M, #平移矩阵
                             (w,h)) #输出图像大小
    return shifted


def rotate(im,angle,center=None,scale=1):
    """

    :param im: #原始图像
    :param angle: #旋转角度
    :param center: #旋转中心
    :param scale: #缩放比例
    :return: #返回经过旋转后的图像
    """

    h, w = im.shape[:2]  # 取出原图像的高度、宽度

    # 计算图像的旋转中心
    if center is None:
        center = (w/2, h/2)

    # 定义旋转矩阵
    M = cv2.getRotationMatrix2D(center,angle,scale)

    # 调用warpAffine函数实现平移变换
    shifted = cv2.warpAffine(im,  # 原始图像
                             M,  # 平移矩阵
                             (w, h))  # 输出图像大小
    return shifted




if __name__ == '__main__':
    im = cv2.imread("data/Linus.png")
    cv2.imshow("im",im)

    # 两个方向平移
    shifted = translate(im, -20 ,50)
    cv2.imshow("shifted_2",shifted)

    shifted = rotate(shifted,-15,center=(50,50),scale=1.5)
    cv2.imshow("shifted_rot", shifted)



    cv2.waitKey()
    cv2.destroyAllWindows()