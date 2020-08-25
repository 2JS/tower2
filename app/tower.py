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
        self.serial = serial.Serial(port, baud)
    
    def getSpeed(self):
        return self.speed
    
    def setSpeed(self, speed):
        self.speed = speed
        if speed == 0:
            self.serial.write("stop\n".encode('utf-8'))
            return
        direction = '+' if speed > 0 else '-'
        speed = abs(speed)
        self.serial.write(f"{speed}{direction}\n".encode('utf-8'))
        return

class Heater():
    temperature = 0
    def __init__(self, port):
        self.heater = minimalmodbus.Instrument(port, 1)

    def getTemperature(self):
        self.temperature = self.heater.read_register(101, 2)
        return self.temperature
    
    def setTemperature(self, temperature):
        self.temperature = temperature
        self.heater.write_register(101, int(temperature*10), 2)
        return
