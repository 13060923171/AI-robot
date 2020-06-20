import picamera


# 大概经过60秒之后就会发现视频录制完成。本地生成一个名称为my_video.h264的录制文件。
with picamera.PiCamera() as camera:
    camera.resolution = (640, 480)
    camera.start_recording('my_video.h264')
    camera.wait_recording(60)
    camera.stop_recording()