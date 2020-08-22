from gpiozero import DigitalOutputDevice
import time
#import sys

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
	now = time.localtime()
	time.sleep(60)
	if(now.tm_hour >= 19 or now.tm_hour < 1):
		signal.off()
	else:
		signal.on()
		
