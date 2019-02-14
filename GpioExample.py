# # # A easy Gpio library example for the Udoo Neo created by David Smerkous
# # # The current things this library can do
# #
# # # digitalWriting/Reading - Soon to come PWM
# #
# # from neo import Gpio  # import Gpio library
# # from time import sleep  # import sleep to wait for blinks
# #
# # neo = Gpio()  # create new Neo object
# #
# # pinTwo = 24  # pin to use
# # pinThree = 25
# # pinFour = 26  # pin to use
# # pinFive = 27
# # pinSix = 2
# #
# # neo.pinMode(pinTwo, neo.OUTPUT)  # Use innerbank pin 2 and set it as output either 0 (neo.INPUT) or 1 (neo.OUTPUT)
# # neo.pinMode(pinThree, neo.OUTPUT)
# # neo.pinMode(pinFour, neo.OUTPUT)
# # neo.pinMode(pinFive, neo.OUTPUT)
# # neo.pinMode(pinSix, neo.INPUT)  # Use pin three(innerbank) and read set state to read
#
# # # Blink example
# # for a in range(0, 5):  # Do for five times
# #     neo.digitalWrite(pinThree, neo.HIGH)  # write high value to pin
# #     sleep(1)  # wait one second
# #     neo.digitalWrite(pinThree, neo.LOW)  # write low value to pin
# #     sleep(1)  # wait one second
# #     neo.digitalWrite(pinFive, neo.HIGH)  # write high value to pin
# #     sleep(1)  # wait one second
# #     neo.digitalWrite(pinFive, neo.LOW)  # write low value to pin
# #     sleep(1)  # wait one second
#
#
#
#
# # Read pin
# # print ("Current pin(" + str(pinThree) + ") state is: " + str(neo.digitalRead(pinThree)))  # read current value of pinThree(To succesfully read a pin it must be either pulled to ground or 3.3v, a non connected wire will not work)
#
#
# #
# #
# # from neo import Gpio
# # from time import sleep
# #
# # neo = Gpio()
# #
# # pinNum = [24, 25, 26, 27]
# #
# # for i in pinNum:
# #     neo.pinMode(pinNum[i], neo.OUTPUT)
# #
# # while 1 :
# # 	for x in range(16):
# # 			num = [0,0,0,0]
# # 			t = x
# # 			for y in range(4):
# # 				num[y] = t%2
# # 				t = t/2
# #
# # 			neo.digitalWrite(pinNum[3], num[3])
# # 			neo.digitalWrite(pinNum[2], num[2])
# # 			neo.digitalWrite(pinNum[1], num[1])
# # 			neo.digitalWrite(pinNum[0], num[0])
# # 			sleep(1)
#
#
# # A easy Gpio library example for the Udoo Neo created by David Smerkous
# # The current things this library can do
#
# # digitalWriting/Reading - Soon to come PWM
# #
# # from neo import Gpio  # import Gpio library
# # from time import sleep  # import sleep to wait for blinks
# #
# # neo = Gpio()  # create new Neo object
# #
# # S0 = 2  # pin to use
# # S1 = 3
# # S2 = 4
# # S3 = 5
# #
# # neo.pinMode(S0, neo.OUTPUT)  # Use innerbank pin 2 and set it as output either 0 (neo.INPUT) or 1 (neo.OUTPUT)
# # neo.pinMode(S1, neo.OUTPUT)  # Use innerbank pin 2 and set it as output either 0 (neo.INPUT) or 1 (neo.OUTPUT)
# # neo.pinMode(S2, neo.OUTPUT)  # Use innerbank pin 2 and set it as output either 0 (neo.INPUT) or 1 (neo.OUTPUT)
# # neo.pinMode(S3, neo.OUTPUT)  # Use innerbank pin 2 and set it as output either 0 (neo.INPUT) or 1 (neo.OUTPUT)
# #
# # pinNum = [S0, S1, S2, S3]
# # # Blink example
# # for i in range(0, 4):
# #     neo.pinMode(pinNum[i], neo.OUTPUT)
# # while 1 :
# #     for x in range(16):
# #         num = [0,0,0,0]
# #         t = x
# #         print("x is" + str(x))1f2/        print(str(t))
# #         for y in range(4):
# #             num[y] = t%2
# #             t = t//2
# #
# #         neo.digitalWrite(pinNum[S3], num[S3])
# #         neo.digitalWrite(pinNum[S2], num[S2])
# #         neo.digitalWrite(pinNum[S1], num[S1])
# #         neo.digitalWrite(pinNum[S0], num[S0])
# #         sleep(1)
# #
# #
# #
#
# A easy Gpio library example for the Udoo Neo created by David Smerkous
# The current things this library can
# from neo import Gpio  # import Gpio library
# from time import sleep  # import sleep to wait for blinks
#
# neo =Gpio()
#
# pinTwo = 2  # pin to use
# pinFour = 3
# pinFive = 4
# pinSix = 25
#
# pinNum = [pinTwo, pinFour, pinFive, pinSix]
#
# # Blink example
# # for i in pinNum:
# #     neo.pinMode(pinNum[i], neo.OUTPUT)
#
# num = [0,0,0,0]
#
# #while 1:
# for x in range(0,16):
#     t = x
#     for y in range(4,0):
#         num[y] = t % 2
#         t = t // 2
#
#     neo.digitalWrite(pinNum[3], num[3])
#     neo.digitalWrite(pinNum[2], num[2])
#     neo.digitalWrite(pinNum[1], num[1])
#     neo.digitalWrite(pinNum[0], num[0])
#     sleep(1)
# A easy Gpio library example for the Udoo Neo created by David Smerkous
# The current things this library can
#


from neo import Gpio  # import Gpio library
from time import sleep
# import sleep to wait for blinks

neo =Gpio()

S0 = 2 # pin to use
S1 = 3
S2 = 4
S3 = 5

pinNum = [S0, S1, S2, S3]

num = [0,0,0,0]

# Blink example
for i in range(4):
    neo.pinMode(pinNum[i], neo.OUTPUT)

neo.digitalWrite(pinNum[0], 0)
# sleep(0.5)
neo.digitalWrite(pinNum[1], 0)
# sleep(0.5)
neo.digitalWrite(pinNum[2], 0)
# sleep(0.5)
neo.digitalWrite(pinNum[3], 0)
# sleep(0.5)

neo.digitalWrite(pinNum[0], 1)
neo.digitalWrite(pinNum[1], 0)
neo.digitalWrite(pinNum[2], 0)
neo.digitalWrite(pinNum[3], 0)

neo.digitalWrite(pinNum[0], 0)
neo.digitalWrite(pinNum[1], 1)
neo.digitalWrite(pinNum[2], 0)
neo.digitalWrite(pinNum[3], 0)

neo.digitalWrite(pinNum[0], 1)
neo.digitalWrite(pinNum[1], 1)
neo.digitalWrite(pinNum[2], 0)
neo.digitalWrite(pinNum[3], 0)

neo.digitalWrite(pinNum[0], 0)
neo.digitalWrite(pinNum[1], 0)
neo.digitalWrite(pinNum[2], 1)
neo.digitalWrite(pinNum[3], 0)

neo.digitalWrite(pinNum[0], 1)
neo.digitalWrite(pinNum[1], 0)
neo.digitalWrite(pinNum[2], 1)
neo.digitalWrite(pinNum[3], 0)

neo.digitalWrite(pinNum[0], 0)
neo.digitalWrite(pinNum[1], 1)
neo.digitalWrite(pinNum[2], 1)
neo.digitalWrite(pinNum[3], 0)

neo.digitalWrite(pinNum[0], 1)
neo.digitalWrite(pinNum[1], 1)
neo.digitalWrite(pinNum[2], 1)
neo.digitalWrite(pinNum[3], 0)

neo.digitalWrite(pinNum[0], 0)
neo.digitalWrite(pinNum[1], 0)
neo.digitalWrite(pinNum[2], 0)
neo.digitalWrite(pinNum[3], 1)

neo.digitalWrite(pinNum[0], 1)
neo.digitalWrite(pinNum[1], 0)
neo.digitalWrite(pinNum[2], 0)
neo.digitalWrite(pinNum[3], 1)

neo.digitalWrite(pinNum[0], 0)
neo.digitalWrite(pinNum[1], 1)
neo.digitalWrite(pinNum[2], 0)
neo.digitalWrite(pinNum[3], 1)

neo.digitalWrite(pinNum[0], 1)
neo.digitalWrite(pinNum[1], 1)
neo.digitalWrite(pinNum[2], 0)
neo.digitalWrite(pinNum[3], 1)

neo.digitalWrite(pinNum[0], 0)
neo.digitalWrite(pinNum[1], 0)
neo.digitalWrite(pinNum[2], 1)
neo.digitalWrite(pinNum[3], 1)

neo.digitalWrite(pinNum[0], 1)
neo.digitalWrite(pinNum[1], 0)
neo.digitalWrite(pinNum[2], 1)
neo.digitalWrite(pinNum[3], 1)

neo.digitalWrite(pinNum[0], 0)
neo.digitalWrite(pinNum[1], 1)
neo.digitalWrite(pinNum[2], 1)
neo.digitalWrite(pinNum[3], 1)

neo.digitalWrite(pinNum[0], 1)
neo.digitalWrite(pinNum[1], 1)
neo.digitalWrite(pinNum[2], 1)
neo.digitalWrite(pinNum[3], 1)

raw = int(open("/sys/bus/iio/devices/iio:device0/in_voltage0_raw").read())
scale = float(open("/sys/bus/iio/devices/iio:device0/in_voltage_scale").read())
print(raw * scale)
