from gpiozero import DigitalOutputDevice
import time

signal = DigitalOutputDevice(14)

print("Running")

while True:
	now = time.localtime()
	if(now.tm_min >= 56):
		signal.on()
	else:
		signal.off()
		
