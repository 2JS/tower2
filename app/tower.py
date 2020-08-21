import os
import serial

class Tower:
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
    speed = 0
    def getSpeed(self):
        return self.speed
    
    def setSpeed(self, speed):
        self.speed = speed
        return

class Fiber(Device):
    speed = 0
    def getSpeed(self):
        return self.speed
    
    def setSpeed(self, speed):
        self.speed = speed
        return

class Heater(Device):
    temperature = 30
    def getTemperature(self):
        return self.temperature
    
    def setTemperature(self, temperature):
        self.temperature = temperature
        return
