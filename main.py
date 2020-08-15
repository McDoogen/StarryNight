from gpiozero import DigitalOutputDevice
import time

signal = DigitalOutputDevice(4)


while True:
	now = time.localtime()
	if(now.tm_min >= 52):
		signal.on()
	else:
		signal.off()
		
