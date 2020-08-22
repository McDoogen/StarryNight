from gpiozero import DigitalOutputDevice
import time

signal = DigitalOutputDevice(14)

print("Running")

while True:
	now = time.localtime()
	if(now.tim_hour >= 19 or now.tim_hour < 1):
		signal.off()
	else:
		signal.on()
		
