from signalstate import *
from relaystate import *

class SignalCollection:

    lamp = None
    pigear = None

    def __init__(self, lamp, pigear):
        self.lamp = lamp
        self.pigear = pigear

    def state(self):
        lampOn = self.lamp.state() == RelayState.on
        pigearOn = self.pigear.state() == RelayState.on

        if lampOn and pigearOn:
            return SignalState.on
        elif lampOn and not pigearOn:
            return SignalState.lampOnly
        elif not lampOn and pigearOn:
            return SignalState.pigearOnly
        else:
            return SignalState.off

    def on(self):
        self.lamp.on()
        self.pigear.on()

    def off(self):
        self.lamp.off()
        self.pigear.off()
