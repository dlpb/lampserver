import unittest
from mockrelay import *
from enum import Enum


class SignalState(Enum):
    off = 1
    lampOnly = 2
    pigearOnly = 4
    on = 8


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
        if self.lamp.state() and self.pigear.state():
            return SignalState.on
        elif self.lamp.state() and not self.pigear.state():
            return SignalState.lampOnly
        elif not self.lamp.state() and self.pigear.state():
            return SignalState.pigearOnly
        else:
            return SignalState.off

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
        self.assertEqual(signals.red.state(), SignalState.off)

    def testWhenCreatingSignalBoard_greenLightsAreOff(self):
        red = None
        green = SignalCollection(Signal(MockRelay()), Signal(MockRelay()))
        signals = SignalBoard(red, green)
        self.assertEquals(signals.green.state(), SignalState.off)

    def testWhenRedSignalIsOff_allRedLightsCanBeTurnedOn(self):
        redLampRelay = MockRelay()
        redPigearRelay = MockRelay()
        red = SignalCollection(Signal(redLampRelay), Signal(redPigearRelay))
        green = None
        signals = SignalBoard(red, green)
        self.assertEquals(signals.red.state(), SignalState.off)
        self.assertFalse(redLampRelay.state())
        self.assertFalse(redPigearRelay.state())

        signals.red.on()
        self.assertEquals(signals.red.state(), SignalState.on)
        self.assertTrue(redLampRelay.state())
        self.assertTrue(redPigearRelay.state())

    def testWhenRedSignalIsOn_allRedLightsCanBeTurnedOff(self):
        redLampRelay = MockRelay()
        redPigearRelay = MockRelay()
        red = SignalCollection(Signal(redLampRelay), Signal(redPigearRelay))
        green = None
        signals = SignalBoard(red, green)

        signals.red.on()
        self.assertEquals(signals.red.state(), SignalState.on)
        self.assertTrue(redLampRelay.state())
        self.assertTrue(redPigearRelay.state())

        signals.red.off()
        self.assertEquals(signals.red.state(), SignalState.off)
        self.assertFalse(redLampRelay.state())
        self.assertFalse(redPigearRelay.state())

    def testWhenRedSignalsAreOff_redLampOnlyCanBeTurnedOn(self):
        redLampRelay = MockRelay()
        redPigearRelay = MockRelay()
        red = SignalCollection(Signal(redLampRelay), Signal(redPigearRelay))
        green = None
        signals = SignalBoard(red, green)

        signals.red.lamp.on()
        self.assertEquals(signals.red.state(), SignalState.lampOnly)
        self.assertTrue(redLampRelay.state())
        self.assertFalse(redPigearRelay.state())

    def testWhenRedSignalsAreOff_redPigearOnlyCanBeTurnedOn(self):
        redLampRelay = MockRelay()
        redPigearRelay = MockRelay()
        red = SignalCollection(Signal(redLampRelay), Signal(redPigearRelay))
        green = None
        signals = SignalBoard(red, green)

        signals.red.pigear.on()
        self.assertEquals(signals.red.state(), SignalState.pigearOnly)
        self.assertTrue(redPigearRelay.state())
        self.assertFalse(redLampRelay.state())

    def testWhenGreenSignalIsOff_allGreenLightsCanBeTurnedOn(self):
        greenLampRelay = MockRelay()
        greenPigearRelay = MockRelay()
        red = None
        green = SignalCollection(Signal(greenLampRelay), Signal(greenPigearRelay))
        signals = SignalBoard(red, green)
        self.assertEquals(signals.green.state(), SignalState.off)

        signals.green.on()
        self.assertEquals(signals.green.state(), SignalState.on)

    def testWhenGreenSignalIsOn_allGreenLightsCanBeTurnedOff(self):
        greenLampRelay = MockRelay()
        greenPigearRelay = MockRelay()
        red = None
        green = SignalCollection(Signal(greenLampRelay), Signal(greenPigearRelay))
        signals = SignalBoard(red, green)

        signals.green.on()
        self.assertEquals(signals.green.state(), SignalState.on)

        signals.green.off()
        self.assertEquals(signals.green.state(), SignalState.off)

    def testWhenGreenSignalsAreOff_greenLampOnlyCanBeTurnedOn(self):
        greenLampRelay = MockRelay()
        greenPigearRelay = MockRelay()
        red = None
        green = SignalCollection(Signal(greenLampRelay), Signal(greenPigearRelay))
        signals = SignalBoard(red, green)

        signals.green.lamp.on()
        self.assertEquals(signals.green.state(), SignalState.lampOnly)

    def testWhenGreenSignalsAreOff_greenPigearOnlyCanBeTurnedOn(self):
        greenLampRelay = MockRelay()
        greenPigearRelay = MockRelay()
        red = None
        green = SignalCollection(Signal(greenLampRelay), Signal(greenPigearRelay))
        signals = SignalBoard(red, green)

        signals.green.pigear.on()
        self.assertEquals(signals.green.state(), SignalState.pigearOnly)


def main():
    unittest.main()

if __name__ == '__main__':
    main()