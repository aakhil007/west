import picamera
from time import sleep
import datetime
camera = picamera.PiCamera()
#str(datetime.datetime.now())[11:22].replace(":","").replace(".","")
try:
	for i in range(2,40):
		a=str(datetime.datetime.now())[11:22].replace(":","").replace(".","")
		camera.capture(str(a)+".jpg")
		print i
		sleep(0.2)	
except KeyboardInterrupt as e:
        pass
finally:
	camera.close()
