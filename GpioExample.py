# A easy Gpio library example for the Udoo Neo created by David Smerkous
# The current things this library can do

# digitalWriting/Reading - Soon to come PWM

from neo import Gpio  # import Gpio library
from time import sleep  # import sleep to wait for blinks

neo = Gpio()  # create new Neo object

pinTwo = 8  # pin to use
pinThree = 9
pinFour = 10  # pin to use
pinFive = 11
pinSix = 2

neo.pinMode(pinTwo, neo.OUTPUT)  # Use innerbank pin 2 and set it as output either 0 (neo.INPUT) or 1 (neo.OUTPUT)
neo.pinMode(pinSix, neo.INPUT)  # Use pin three(innerbank) and read set state to read
neo.pinMode(pinThree, neo.OUTPUT)  # Use innerbank pin 2 and set it as output either 0 (neo.INPUT) or 1 (neo.OUTPUT)
neo.pinMode(pinSix, neo.INPUT)
neo.pinMode(pinFour, neo.OUTPUT)  # Use innerbank pin 2 and set it as output either 0 (neo.INPUT) or 1 (neo.OUTPUT)
neo.pinMode(pinSix, neo.INPUT)
neo.pinMode(pinFive, neo.OUTPUT)  # Use innerbank pin 2 and set it as output either 0 (neo.INPUT) or 1 (neo.OUTPUT)
neo.pinMode(pinSix, neo.INPUT)

# Blink example
for a in range(0, 5):  # Do for five times
    neo.digitalWrite(pinThree, neo.HIGH)  # write high value to pin
    sleep(1)  # wait one second
    neo.digitalWrite(pinThree, neo.LOW)  # write low value to pin
    sleep(1)  # wait one second
    neo.digitalWrite(pinFive, neo.HIGH)  # write high value to pin
    sleep(1)  # wait one second
    neo.digitalWrite(pinFive, neo.LOW)  # write low value to pin
    sleep(1)  # wait one second

    neo.digitalWrite(pinTwo, neo.HIGH)  # write high value to pin
    sleep(1)  # wait one second
    neo.digitalWrite(pinTwo, neo.LOW)  # write low value to pin
    sleep(1)  # wait one second
    neo.digitalWrite(pinFive, neo.HIGH)  # write high value to pin
    sleep(1)  # wait one second
    neo.digitalWrite(pinFive, neo.LOW)  # write low value to pin
    sleep(1)  # wait one second

    neo.digitalWrite(pinTwo, pinFive, neo.HIGH)  # write high value to pin
    sleep(1)  # wait one second
    neo.digitalWrite(pinTwo, pinFive, neo.LOW)  # write low value to pin
    sleep(1)  # wait one second
    neo.digitalWrite(pinThree, pinFive, neo.HIGH)  # write high value to pin
    sleep(1)  # wait one second
    neo.digitalWrite(pinThree, pinFive, neo.LOW)  # write low value to pin
    sleep(1)  # wait one second
    neo.digitalWrite(pinFour, pinFive, neo.HIGH)  # write high value to pin
    sleep(1)  # wait one second
    neo.digitalWrite(pinFour, pinFive, neo.LOW)  # write low value to pin
    sleep(1)  # wait one second
    neo.digitalWrite(pinFive, neo.HIGH)  # write high value to pin
    sleep(1)  # wait one second
    neo.digitalWrite(pinFive, neo.LOW)  # write low value to pin
    sleep(1)  # wait one second


# Read pin
print ("Current pin(" + str(pinThree) + ") state is: " + str(neo.digitalRead(pinThree)))  # read current value of pinThree(To succesfully read a pin it must be either pulled to ground or 3.3v, a non connected wire will not work)
