from picamera import PiCamera
from time import sleep
import time

camera = PiCamera()
camera.rotation = 180

camera.start_preview()
#sleep(10)
t1 = time.time()
camera.capture('/home/pi/Desktop/image.jpg')
t2 = time.time()
print('dt = ' + str(t2-t1))
camera.stop_preview()
