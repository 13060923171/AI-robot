import time
import picamera


'''
方法一：使用命令行方式完成拍照

打开终端输入如下命令：

1.  raspistill -t 2000 -o image1.jpg  

2.  raspistill -t 2000 -o image2.jpg -w 640 -h 480 

第一句命令为：两秒钟延时拍一张照片，保存本地名为imag1.jpg。

第二句命令为：两秒钟延时拍一张照片，保存本地名为imag2.jpg，分辨率为640X480


'''

# 先建立了camera设备，然后设置分辨率为1024X768，开始预览，预热2秒之后，拍照并存本地文件名为foo.jpg。 

with picamera.PiCamera() as camera:
    camera.resolution = (1024, 768)
    camera.start_preview()
    #摄像头预热2秒
    time.sleep(2)
    camera.capture('foo.jpg')