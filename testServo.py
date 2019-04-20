import brooklyn as brd
import time

test = brd.Brooklyn()
test.setcard(1, brd.EMPIRE_STATE)
test.setcard(2, brd.EMPIRE_STATE)
test.setcard(3, brd.EMPIRE_STATE)
test.setcard(4, brd.EMPIRE_STATE)

test.begin()

servo1 = test.getservo(4, 4)
servo1.defineangle(280)
servo1.setangle(0)
time.sleep(3)
servo1.setangle(140)
time.sleep(3)
servo1.setangle(200)
time.sleep(3)
servo1.setangle(280)
time.sleep(2)
servo1.setangle(140)
time.sleep(2)
servo1.setangle(280)