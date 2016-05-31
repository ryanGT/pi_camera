from picamera import PiCamera
from time import sleep
import time

camera = PiCamera()
camera.rotation = 180# image was upside down
camera.brightness = 60# default brightness is 50; this makes the
                      # picture slightly brighter through longer
                      # exposure
#camera.ISO = 800
camera.ISO = 1600
camera.start_preview()# I think this basically turns the camera on

import os
#rootdir = '/home/pi/baby_monitor'
rootdir = '/home/pi/git/cherrypy_learn/img/'
if not os.path.exists(rootdir):
    os.mkdir(rootdir)

foldername = time.strftime('%m_%d_%y')
folderpath = os.path.join(rootdir, foldername)
print('folderpath: ' + folderpath)

if not os.path.exists(folderpath):
    os.mkdir(folderpath)
    
t1 = time.time()
runtime = 180.0*60# 30 minutes, expressed in seconds
endtime = t1 + runtime
curtime = time.time()
while curtime < endtime:
    filename = time.strftime('image_%I_%M_%S_%p.jpg')
    filepath = os.path.join(folderpath, filename)
    print(filepath)
    camera.capture(filepath)
    time.sleep(10.0)# wait 10 seconds before next picture
    
camera.stop_preview()
