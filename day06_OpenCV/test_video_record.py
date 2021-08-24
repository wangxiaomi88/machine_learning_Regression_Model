#录制视频文件
#两个过程：读取、写入文件
import cv2

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc("I","4","2","0") #编解码4字标记值说明
"""
编解码4字标记值说明
cV2. Videowriter fourcc('I',"4',"2',"0")表示未压缩的Yuv颜色编码格式,色度子采样为4:2:0。
该编码格式具有较好的兼容性,但产生的文件较大,文件扩展名为.avi。
cv2. Videowriter_ fourcc("P","I',"M',"I")表示MPEG-1编码类型,生成的文件的扩展名为.avi。
cv2. videowriter fourcc("X","V","I","D")表示MPEG-4编码类型。如果希望得到的视频大小为平均值,可以选用这个参数组合
该组合生成的文件的扩展名为.av1。
cV2. Videowriter fourcc("T","H","E","O")表示 ogg Vorbis编码类型,文件的扩展名为.ogv。
cv2. Videowriter_ fourcc("F","L","V","I")表示F1ash视频,生成的文件的扩展名为.flv。
"""

out = cv2.VideoWriter("output.avi", #存储的视频文件名
                      fourcc, #编解码格式
                      20, #帧速率
                      (640,480)) #分辨率

while cap.isOpened():
    ret, frame = cap.read()  # 捕获帧

    if ret == True:
        out.write(frame)
        cv2.imshow("frame", frame)
        if cv2.waitKey(1)==27:
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()



