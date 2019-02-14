from neo import easyGpio
from time import sleep

pin = easyGpio(24) # Pin 2 with LED
pin = easyGpio(25)
pin = easyGpio(26)
pin = easyGpio(27)
readpin = easyGpio(A0) # Pin 3 with switch

pin.pinOUT() # Make pin output 
readpin.pinIN() # Make pin in

while True:
	pin.on() # Turn pin on
	sleep(1) # wait one second
	pin.off() # Turn pin off
	print ("pin 3 state %d" % readpin.get()) # Get current pin state
	sleep(1)
