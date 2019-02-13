# # A easy Gpio library example for the Udoo Neo created by David Smerkous
# # The current things this library can do
#
# # digitalWriting/Reading - Soon to come PWM
#
# from neo import Gpio  # import Gpio library
# from time import sleep  # import sleep to wait for blinks
#
# neo = Gpio()  # create new Neo object
#
# pinTwo = 24  # pin to use
# pinThree = 25
# pinFour = 26  # pin to use
# pinFive = 27
# pinSix = 2
#
# neo.pinMode(pinTwo, neo.OUTPUT)  # Use innerbank pin 2 and set it as output either 0 (neo.INPUT) or 1 (neo.OUTPUT)
# neo.pinMode(pinThree, neo.OUTPUT)
# neo.pinMode(pinFour, neo.OUTPUT)
# neo.pinMode(pinFive, neo.OUTPUT)
# neo.pinMode(pinSix, neo.INPUT)  # Use pin three(innerbank) and read set state to read
#
# # Blink example
# for a in range(0, 5):  # Do for five times
#     neo.digitalWrite(pinThree, neo.HIGH)  # write high value to pin
#     sleep(1)  # wait one second
#     neo.digitalWrite(pinThree, neo.LOW)  # write low value to pin
#     sleep(1)  # wait one second
#     neo.digitalWrite(pinFive, neo.HIGH)  # write high value to pin
#     sleep(1)  # wait one second
#     neo.digitalWrite(pinFive, neo.LOW)  # write low value to pin
#     sleep(1)  # wait one second
#
# # Read pin
# print ("Current pin(" + str(pinThree) + ") state is: " + str(neo.digitalRead(pinThree)))  # read current value of pinThree(To succesfully read a pin it must be either pulled to ground or 3.3v, a non connected wire will not work)
#
#


from neo import Gpio
from time import sleep

neo = Gpio()

pinNum = [24, 25, 26, 27]

for i in pinNum:
    neo.pinMode(pinNum[4], neo.OUTPUT)

while 1 :
	for x in range(16):
			num = [0,0,0,0]
			t = x
			for y in range(4):
				num[y] = t%2
				t = t/2

			neo.digitalWrite(pinNum[3], num[3])
			neo.digitalWrite(pinNum[2], num[2])
			neo.digitalWrite(pinNum[1], num[1])
			neo.digitalWrite(pinNum[0], num[0])
			sleep(1)
