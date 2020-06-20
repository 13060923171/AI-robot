# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

# initialize the camera and grab a reference to the raw camera capture
'''
首先通过piCamera库来完成摄像头创建和分辨率设置，经过1s的预热之后，通过摄像头来采集连续帧，然后从帧中取出image来通过cv2窗口接口imshow来显示出来，
最后清除流存储空间，并查找键盘key是否是q如果是q的话就退出视频传输。
结果输出：我们会看到一个640X480大小的视频流监控框。基本实现了我们的实验预期效果
'''
camera = PiCamera()
camera.resolution = (640, 480) # 分辨率设置
camera.framerate = 32 # 帧率设置
rawCapture = PiRGBArray(camera, size=(640, 480)) # 视频参数

# allow the camera to warmup
time.sleep(1)

 

# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True): # bgr颜色
    # grab the raw NumPy array representing the image, then initialize the timestamp
    # and occupied/unoccupied text
    image = frame.array # 图片矩阵（数组）
    # show the frame
    cv2.imshow("Frame", image)
    key = cv2.waitKey(1) & 0xFF
    # clear the stream in preparation for the next frame
    rawCapture.truncate(0) # truncate 中断
    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break