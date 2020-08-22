from gpiozero import DigitalOutputDevice
import time, sys

signal = DigitalOutputDevice(14)

print("Running")
#print(sys.argv[1])
#if(sys.argv[1] == '0'):
#	print("Turn off")
#	signal.on()
#elif(sys.argv[1] == '1'):
#	print("Turn on")
#	signal.off()

while True:
	pass
	now = time.localtime()
	if(now.tim_hour >= 19 or now.tim_hour < 1):
		signal.off()
	else:
		signal.on()
		
