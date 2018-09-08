import brooklyn as brd
import time

test = brd.Brooklyn()
test.setcard(1, brd.EMPIRE_STATE)
test.setcard(2, brd.EMPIRE_STATE)
test.setcard(3, brd.EMPIRE_STATE)
test.setcard(4, brd.EMPIRE_STATE)

test.begin()

motor1 = test.getmotor(1)
motor2 = test.getmotor(2)
motor3 = test.getmotor(3)
motor4 = test.getmotor(4)
motor5 = test.getmotor(5)
motor6 = test.getmotor(6)
motor7 = test.getmotor(7)
motor8 = test.getmotor(8)

time.sleep(2)
motor1.setPWM(255)
time.sleep(2)
motor2.setPWM(255)
time.sleep(2)
motor3.setPWM(255)
time.sleep(2)
motor4.setPWM(255)
time.sleep(2)
motor5.setPWM(255)
time.sleep(2)
motor6.setPWM(255)
time.sleep(2)
motor7.setPWM(255)
time.sleep(2)
motor8.setPWM(255)


