import io
import picamera
import cv2
import numpy
'''

我们使用与树莓派原装摄像头匹配的picamera程序库来获取图片信息然后利用opencv的人脸库来识别是否有人脸，
其中haarcascade_frontalface_alt.xml，就是opencv自带的人脸模型库，我们就是利用这个识别出人脸的。
这个路径下还有眼睛、鼻子、人体等模型库，你也可以换成相应的模型做相应的识别。

'''
#Create a memory stream so photos doesn't need to be saved in a file
stream = io.BytesIO()
#Get the picture (low resolution, so it should be quite fast)
#Here you can also specify other parameters (e.g.:rotate the image)
with picamera.PiCamera() as camera:
	camera.resolution = (320, 240)
	camera.capture(stream, format='jpeg')
#Convert the picture into a numpy array
buff = numpy.fromstring(stream.getvalue(), dtype=numpy.uint8)
#Now creates an OpenCV image
image = cv2.imdecode(buff, 1)
#Load a cascade file for detecting faces
face_cascade = cv2.CascadeClassifier('/usr/share/opencv/haarcascades/haarcascade_frontalface_alt.xml')
#Convert to grayscale
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#Look for faces in the image using the loaded cascade file
faces = face_cascade.detectMultiScale(gray, 1.1, 5)
print "Found "+str(len(faces))+" face(s)"
#Draw a rectangle around every found face
for (x,y,w,h) in faces:
	cv2.rectangle(image,(x,y),(x+w,y+h),(255,255,0),2)
	#Save the result image
	cv2.imwrite('result.jpg',image)
	cv2.imshow('face_detect', image)
	c = cv2.waitKey(0)
	cv2.destroyAllWindows()