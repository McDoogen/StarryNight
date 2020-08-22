from gpiozero import DigitalOutputDevice
import time, sys

signal = DigitalOutputDevice(14)

print("Running")

if(sys.argv[1] == 0):
	signal.on()
elif(sys.argv[1] == 1):
	signal.off()

while True:
	#now = time.localtime()
	#if(now.tim_hour >= 19 or now.tim_hour < 1):
	#	signal.off()
	#else:
	#	signal.on()
		
