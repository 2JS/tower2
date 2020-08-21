import os
import serial

class tower:
    def __init__(self):
        self.connect()

    def connect(self,
            stepper1=os.environ["STEPPER1_DEV"],
            stepper2=os.environ["STEPPER2_DEV"],
            heater=os.environ["HEATER_DEV"]
        ):
        self.stepper1 = serial.Serial(
            port=stepper1,
            baudrate=115200
        )

        self.stepper2 = serial.Serial(
            port=stepper2,
            baudrate=115200
        )

        self.heater = serial.Serial(
            port=heater,
            baudrate=19200
        )

        # micrometer = serial.Serial(
        #     port=os.environ["MICROMETER_DEV"],
        #     baudrate=os.environ["MICROMETER_BAUD"]
        # )

        return self.stepper1, self.stepper2, self.heater

    def disconnect(self):
        self.stepper1.close()
        self.stepper2.close()
        self.heater.close()

class Extruder(Device):
    def getSpeed(self):
        return 0
    
    def setSpeed(self, speed):
        return

class Fiber(Device):
    def getSpeed(self):
        return 0
    
    def setSpeed(self, speed):
        return

class Heater(Device):
    def getTemperature(self):
        return 0
    
    def setTemperature(self, temperature):
        return
