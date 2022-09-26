import picamera
import time
camera = picamera.PiCamera()
camera.vflip = True
camera.start_preview()
time.sleep(1)
camera.capture ('/home/pi/Desktop/image5.jpg')
camera.stop_preview
