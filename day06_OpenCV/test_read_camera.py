# 从摄像头读取图像并播放
import cv2

cap = cv2.VideoCapture(0) #实例化VideoCapture对象，参数0表示第一个摄像头
while cap.isOpened(): #摄像头处于打开状态
    ret,frame = cap.read() #捕获帧
    cv2.imshow("frame",frame)

    c =cv2.waitKey(1) #等待1ms，等待用户敲击按键
    if c == 27: #Esc键
        break


cap.release()
cv2.destroyAllWindows()




