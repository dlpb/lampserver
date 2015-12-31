import unittest
from mockrelay import *

class Signal:
    relay = None

    def __init__(self, relay):
        self.relay = relay

    def state(self):
        return self.relay.state()

    def on(self):
        self.relay.on()



class SignalCollection:

    lamp = None
    pigear = None

    def __init__(self, lamp, pigear):
        self.lamp = lamp
        self.pigear = pigear

    def state(self):
        return self.lamp.state() and self.pigear.state()

    def on(self):
        self.lamp.on()
        self.pigear.on()


class SignalBoard:
    red = None
    green = None

    def __init__(self, red, green):
        self.red = red
        self.green = green


class SignalBoardTests(unittest.TestCase):

    def testWhenCreatingSignalBoard_redLightsAreOff(self):

        red = SignalCollection(Signal(None), Signal(None))
        green = None
        signals = SignalBoard(red, green)
        self.assertFalse(signals.red.state())

    def testWhenCreatingSignalBoard_greenLightsAreOff(self):
        red = None
        green = SignalCollection(Signal(None), Signal(None))
        signals = SignalBoard(red, green)
        self.assertFalse(signals.green.state())

    def testWhenRedSignalIsOff_allRedLightsCanBeTurnedOn(self):
        red = SignalCollection(Signal(MockRelay()), Signal(MockRelay()))
        green = None
        signals = SignalBoard(red, green)
        signals.red.on()
        self.assertTrue(signals.red.state())



def main():
    unittest.main()

if __name__ == '__main__':
    main()