from relaystate import RelayState

import smbus
import signal
import sys

bus = smbus.SMBus(1)    # 0 = /dev/i2c-0 (port I2C0), 1 = /dev/i2c-1 (port I2C1)

def endProcess(signalnum = None, handler = None):
    DEVICE_ADDRESS = 0x20      #7 bit address (will be left shifted to add the read write bit)
    DEVICE_REG_MODE1 = 0x06
    DEVICE_REG_DATA = 0xff
    DEVICE_REG_DATA |= (0xf<<0)
    bus.write_byte_data(DEVICE_ADDRESS, DEVICE_REG_MODE1, DEVICE_REG_DATA)
    sys.exit()

signal.signal(signal.SIGINT, endProcess)

class Relay:

    global bus

    __state__ = RelayState.off
    number = 0

    def __init__(self, number = 0):
        self.number = number
        self.DEVICE_ADDRESS = 0x20      #7 bit address (will be left shifted to add the read write bit)
        self.DEVICE_REG_MODE1 = 0x06
        self.DEVICE_REG_DATA = 0xff
        bus.write_byte_data(self.DEVICE_ADDRESS, self.DEVICE_REG_MODE1, self.DEVICE_REG_DATA)

    def on(self):
        self.__state__ = RelayState.on
        self.DEVICE_REG_DATA &= ~(0x1<<self.number)
        bus.write_byte_data(self.DEVICE_ADDRESS, self.DEVICE_REG_MODE1, self.DEVICE_REG_DATA)

    def off(self):
        self.__state__ = RelayState.off
        self.DEVICE_REG_DATA |= (0x1<<self.number)
        bus.write_byte_data(self.DEVICE_ADDRESS, self.DEVICE_REG_MODE1, self.DEVICE_REG_DATA)

    def state(self):
        return self.__state__