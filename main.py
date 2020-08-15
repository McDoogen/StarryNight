from gpiozero import DigitalOutputDevice
import time

signal = DigitalOutputDevice(4)


while True:
	now = time.localtime()
	if(now.tm_min >= 54):
		signal.on()
	else:
		signal.off()
		
