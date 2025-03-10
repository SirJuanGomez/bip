import math
from Control import *
from Servo import *
class Action:
    def __init__(self):
        self.servo=Servo()
        self.control=Control()
        self.servo.setServoAngle(15,90)
    def hands_up(self):
        # Transition from [90, 78, 0] to [120, 78, 0]
        xyz=[[90,78,0],[90,78,0],[90,78,0],[90,78,0]]  # Start with [90,78,0]
        for i in range(4):
            xyz[i][0] = (xyz[i][0] - self.control.point[i][0]) / 30
            xyz[i][1] = (xyz[i][1] - self.control.point[i][1]) / 30
            xyz[i][2] = (xyz[i][2] - self.control.point[i][2]) / 30

        for j in range(30):
            for i in range(4):
                self.control.point[i][0] += xyz[i][0]
                self.control.point[i][1] += xyz[i][1]
                self.control.point[i][2] += xyz[i][2]
            self.control.run()
            time.sleep(0.01)

        # Transition back from [120, 78, 0] to [90, 78, 0]
        xyz=[[120,78,0],[120,78,0],[120,78,0],[120,78,0]]  # Now go to [120,78,0]
        for i in range(4):
            xyz[i][0] = (xyz[i][0] - self.control.point[i][0]) / 30
            xyz[i][1] = (xyz[i][1] - self.control.point[i][1]) / 30
            xyz[i][2] = (xyz[i][2] - self.control.point[i][2]) / 30

        for j in range(30):
            for i in range(4):
                self.control.point[i][0] += xyz[i][0]
                self.control.point[i][1] += xyz[i][1]
                self.control.point[i][2] += xyz[i][2]
            self.control.run()
            time.sleep(0.01)

if __name__=='__main__':
    action=Action()  
    time.sleep(2) 
    while True:
        action.hands_up()
        time.sleep(3)