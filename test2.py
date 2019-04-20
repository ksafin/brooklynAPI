import brooklyn as brd
import time

test = brd.Brooklyn()
test.setcard(1, brd.EMPIRE_STATE)
test.setcard(2, brd.EMPIRE_STATE)
test.setcard(3, brd.EMPIRE_STATE)
test.setcard(4, brd.EMPIRE_STATE)

test.begin()

#servo1 = test.getservo(4, 1)
#servo1.defineangle(280)
#servo1.setangle(0)
#time.sleep(3)
#servo1.setangle(140)
#time.sleep(3)
#servo1.setangle(200)
#time.sleep(3)
#servo1.setangle(280)
#time.sleep(2)
#servo1.setangle(140)
#time.sleep(2)
#servo1.setangle(280)

motor1 = test.getmotor(1)
motor2 = test.getmotor(2)
motor3 = test.getmotor(3)
motor4 = test.getmotor(4)
motor5 = test.getmotor(5)
motor6 = test.getmotor(6)
motor7 = test.getmotor(7)
motor8 = test.getmotor(8)

motor1.setPWM(100)
time.sleep(1)
motor2.setPWM(100)
time.sleep(1)
motor3.setPWM(100)
time.sleep(1)
motor4.setPWM(100)
time.sleep(1)
motor5.setPWM(100)
time.sleep(1)
motor6.setPWM(100)
time.sleep(1)
motor7.setPWM(100)
time.sleep(1)
motor8.setPWM(100)
time.sleep(1)


#while True:
#    for i in range(0,249):
#        motor7.setPWM(i)
#        time.sleep(0.1)
    
#    for i in reversed(range(0,249)):
#        motor7.setPWM(i)
#        time.sleep(0.1)

