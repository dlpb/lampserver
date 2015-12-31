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

    def off(self):
        self.relay.off()



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

    def off(self):
        self.lamp.off()
        self.pigear.off()


class SignalBoard:
    red = None
    green = None

    def __init__(self, red, green):
        self.red = red
        self.green = green


class SignalBoardTests(unittest.TestCase):

    def testWhenCreatingSignalBoard_redLightsAreOff(self):
        red = SignalCollection(Signal(MockRelay()), Signal(MockRelay()))
        green = None
        signals = SignalBoard(red, green)
        self.assertFalse(signals.red.state())

    def testWhenCreatingSignalBoard_greenLightsAreOff(self):
        red = None
        green = SignalCollection(Signal(MockRelay()), Signal(MockRelay()))
        signals = SignalBoard(red, green)
        self.assertFalse(signals.green.state())

    def testWhenRedSignalIsOff_allRedLightsCanBeTurnedOn(self):
        redLampRelay = MockRelay()
        redPigearRelay = MockRelay()
        red = SignalCollection(Signal(redLampRelay), Signal(redPigearRelay))
        green = None
        signals = SignalBoard(red, green)
        self.assertFalse(signals.red.state())
        self.assertFalse(redLampRelay.state())
        self.assertFalse(redPigearRelay.state())

        signals.red.on()
        self.assertTrue(signals.red.state())
        self.assertTrue(redLampRelay.state())
        self.assertTrue(redPigearRelay.state())

    def testWhenRedSignalIsOn_allRedLightsCanBeTurnedOff(self):
        redLampRelay = MockRelay()
        redPigearRelay = MockRelay()
        red = SignalCollection(Signal(redLampRelay), Signal(redPigearRelay))
        green = None
        signals = SignalBoard(red, green)

        signals.red.on()
        self.assertTrue(signals.red.state())
        self.assertTrue(redLampRelay.state())
        self.assertTrue(redPigearRelay.state())

        signals.red.off()
        self.assertFalse(signals.red.state())
        self.assertFalse(redLampRelay.state())
        self.assertFalse(redPigearRelay.state())








def main():
    unittest.main()

if __name__ == '__main__':
    main()