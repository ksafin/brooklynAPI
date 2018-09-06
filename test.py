import brooklyn as brd
import time

test = brd.Brooklyn()
test.setcard(2, brd.EMPIRE_STATE)

motor1 = test.getmotor(3)
motor2 = test.getmotor(4)

motor1.setPWM(128)

