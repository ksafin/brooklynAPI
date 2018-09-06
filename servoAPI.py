import packet_util as pu


class Servo:

    # ser = Serial Console Object
    # cid = Component ID (1-8)
    # sid = Servo ID -- Servo 1 or Servo 2
    def __init__(self, ser, cid, sid):
        self.cid = cid
        self.sid = sid
        self.ser = ser
        self.angle = 0

    # Sets servo angle attribute
    def defineangle(self, angle):
        self.angle = angle

    # Set Servo Angle, from 0 to defined angle
    # angle -- a value from 0 to the servos defined angle, to which to advance
    # Function ID: 0x10/0x12 (Servo1/Servo2)
    def setangle(self, angle):
        # Do not execute if angle is out of range or servo is continuous
        if (angle > self.angle) or (angle < 0) or (self.angle == 0):
            return False

        # Convert to proper angle range (0 to 180)
        newangle = int(round(angle * (180.0/float(self.angle))))

        # 0x10 for Servo 1, 0x12 for Servo 2
        pack_sid = 0x10
        if self.sid == 2:
            pack_sid = 0x12

        # Assemble packet and write to USB, return true for success
        packet = pu.getPacket(pack_sid, self.cid, list([newangle]))
        self.ser.write(packet)
        return True

    # Set Speed for continuous servo
    # Speed -- a value from -90 to 90, indicating both direction and speed
    # Function ID: 0x11/0x13 (Servo1/Servo2)
    def setspeed(self, speed):
        # Do not execute if speed is out of range or servo is not continuous
        if (speed > 90) or (speed < -90) or (self.angle != 0):
            return False

        # On motor board, 0 = full reverse, 90 is stop, 180 is full forward
        # Add 90 to produce this result given a -90 to 90 range
        data = list([speed + 90])

        # 0x11 for Servo 1, 0x13 for Servo 2
        pack_sid = 0x11
        if self.sid == 2:
            pack_sid = 0x13

        # Assemble packet and write to USB, return true for success
        packet = pu.getPacket(pack_sid, self.cid, data)
        self.ser.write(packet)
        return True
