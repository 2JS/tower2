import os
import serial
import minimalmodbus

class Tower:
    def __init__(self):
        # self.connect()
        self.heater = Heater(os.environ['TOWER_HEATER_PORT'])
        self.extruder = Stepper(os.environ['TOWER_EXTRUDER_PORT'])
        self.fiber = Stepper(os.environ['TOWER_FIBER_PORT'])
        # self.fiber2 = Stepper('/dev/ttyUSB2')

        self.heater.setTemperature(0)
        self.extruder.setSpeed(0)
        self.fiber.setSpeed(0)

class Stepper():
    speed = 0
    def __init__(self, port, baud=115200):
        # self.serial = serial.Serial(port, baud)
        pass
    
    def getSpeed(self):
        return self.speed
    
    def setSpeed(self, speed):
        self.speed = speed
        if speed == 0:
            # self.serial.write("stop\n")
            return
        direction = '+' if speed > 0 else '-'
        speed = abs(speed)
        # self.serial.write(f"{speed}{direction}\n")
        return

class Heater():
    temperature = 0
    def __init__(self, port):
        # self.heater = minimalmodbus.Instrument(port, 1)
        pass

    def getTemperature(self):
        # self.temperature = self.heater.read_register(1000)
        return self.temperature
    
    def setTemperature(self, temperature):
        self.temperature = temperature
        # self.heater.write_register(1001, int(temperature*10))
        return
