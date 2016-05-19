from picamera import PiCamera
from time import sleep
import time

camera = PiCamera()
camera.rotation = 180
camera.ISO = 1600
camera.start_preview()
#sleep(10)
t1 = time.time()
import os
outdir = '/home/pi/baby_monitor'
if not os.path.exists(outdir):
    os.mkdir(outdir)

for i in range(10):
    filename = 'image_%0.4d.jpg' % i
    filepath = os.path.join(outdir, filename)
    camera.capture(filepath)
    time.sleep(1.0)
    
camera.stop_preview()
