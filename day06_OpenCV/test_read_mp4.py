#读取视频文件并播放
import cv2

import cv2
cap = cv2.VideoCapture("data/video/三国杀.mp4") #实例化VideoCapture对象，打开视频路径
# cap = cv2.VideoCapture("data\\video\\三国杀.mp4") #实例化VideoCapture对象，打开视频路径
while cap.isOpened(): #摄像头处于打开状态
    ret,frame = cap.read() #捕获帧
    cv2.imshow("frame",frame)

    c =cv2.waitKey(15) #等待1ms，等待用户敲击按键
    if c == 27: #Esc键
        break


cap.release()
cv2.destroyAllWindows()

