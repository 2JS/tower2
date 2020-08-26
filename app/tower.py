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
    limit = (-270, 270)
    def __init__(self, port, baud=115200):
        self.serial = serial.Serial(port, baud)
    
    def getSpeed(self):
        return self.speed
    
    def setSpeed(self, speed):
        lower, upper = self.limit
        if lower > speed:
            speed = lower
        if upper < speed:
            speed = upper
        
        self.speed = speed
        if speed == 0:
            self.serial.write("stop\n".encode('utf-8'))
            return
        
        direction = '+' if speed > 0 else '-'
        speed = abs(speed)
        self.serial.write(f"{speed}{direction}\n".encode('utf-8'))

        return
    
    def getLimit(self):
        return self.limit
    
    def setLimit(self, lower, upper):
        if lower < upper:
            self.limit = lower, upper

class Heater():
    temperature = 0
    limit = 350
    def __init__(self, port):
        self.heater = minimalmodbus.Instrument(port, 101)

    def getTemperature(self):
        self.temperature, self.targetTemperature = self.heater.read_register(1000, 2)
        self.on = self.heater.read_register(1015, 1)
        return self.temperature, self.targetTemperature
    
    def setTemperature(self, temperature):
        if (temperature < 0):
            temperature = 0
        if (temperature > 350):
            temperature = 350
        self.temperature = int(temperature)
        self.heater.write_register(1001, int(temperature), 1)
        return
    
    def getLimit(self):
        return self.limit
