import motorAPI
import servoAPI


class EmpireState:
    
    def __init__(self, bay, ser):
        self.bay = bay
        self.ser = ser

        # Initialize both motors with proper Component IDs
        self.motor1 = motorAPI.Motor(self.ser, (bay * 2) - 1)
        self.motor2 = motorAPI.Motor(self.ser, (bay * 2))

        # Initialize Servo 1 & 2, which are controlled by the lower CID
        self.servo1 = servoAPI.Servo(self.ser, (bay * 2) - 1, 1)
        self.servo2 = servoAPI.Servo(self.ser, (bay * 2) - 1, 1)

        # Initialize Servo 3 & 4, which are controlled by the higher CID
        self.servo3 = servoAPI.Servo(self.ser, (bay * 2), 2)
        self.servo4 = servoAPI.Servo(self.ser, (bay * 2), 2)

    def getMotor(self, idx):
        if idx == 0:
            return self.motor1
        elif idx == 1:
            return self.motor2
        else:
            return None

    def getServo(self, idx):
        if idx == 0:
            return self.servo1
        elif idx == 1:
            return self.servo2
        elif idx == 2:
            return self.servo3
        elif idx == 3:
            return self.servo4
        else:
            return None


