import unittest

from main.python.signallight import SignalLight

from mockrelay import MockRelay
from relaystate import RelayState
from signalboard import SignalBoard
from signalcollection import SignalCollection
from signalstate import SignalState


class SignalBoardTests(unittest.TestCase):

    def testWhenCreatingSignalBoard_redLightsAreOff(self):
        red = SignalCollection(SignalLight(MockRelay()), SignalLight(MockRelay()))
        green = None
        signals = SignalBoard(red, green)
        self.assertEqual(signals.red.state(), SignalState.off)

    def testWhenCreatingSignalBoard_greenLightsAreOff(self):
        red = None
        green = SignalCollection(SignalLight(MockRelay()), SignalLight(MockRelay()))
        signals = SignalBoard(red, green)
        self.assertEquals(signals.green.state(), SignalState.off)

    def testWhenRedSignalIsOff_allRedLightsCanBeTurnedOn(self):
        redLampRelay = MockRelay()
        redPigearRelay = MockRelay()
        red = SignalCollection(SignalLight(redLampRelay), SignalLight(redPigearRelay))
        green = None
        signals = SignalBoard(red, green)
        self.assertEquals(signals.red.state(), SignalState.off)
        self.assertEquals(redLampRelay.state(), RelayState.off)
        self.assertEquals(redPigearRelay.state(), RelayState.off)

        signals.red.on()
        self.assertEquals(signals.red.state(), SignalState.on)
        self.assertEquals(redLampRelay.state(), RelayState.on)
        self.assertEquals(redPigearRelay.state(), RelayState.on)

    def testWhenRedSignalIsOn_allRedLightsCanBeTurnedOff(self):
        redLampRelay = MockRelay()
        redPigearRelay = MockRelay()
        red = SignalCollection(SignalLight(redLampRelay), SignalLight(redPigearRelay))
        green = None
        signals = SignalBoard(red, green)

        signals.red.on()
        self.assertEquals(signals.red.state(), SignalState.on)
        self.assertEquals(redLampRelay.state(), RelayState.on)
        self.assertEquals(redPigearRelay.state(), RelayState.on)

        signals.red.off()
        self.assertEquals(signals.red.state(), SignalState.off)
        self.assertEquals(redLampRelay.state(), RelayState.off)
        self.assertEquals(redPigearRelay.state(), RelayState.off)

    def testWhenRedSignalsAreOff_redLampOnlyCanBeTurnedOn(self):
        redLampRelay = MockRelay()
        redPigearRelay = MockRelay()
        red = SignalCollection(SignalLight(redLampRelay), SignalLight(redPigearRelay))
        green = None
        signals = SignalBoard(red, green)

        signals.red.lamp.on()
        self.assertEquals(signals.red.state(), SignalState.lampOnly)
        self.assertEquals(redLampRelay.state(), RelayState.on)
        self.assertEquals(redPigearRelay.state(), RelayState.off)

    def testWhenRedSignalsAreOff_redPigearOnlyCanBeTurnedOn(self):
        redLampRelay = MockRelay()
        redPigearRelay = MockRelay()
        red = SignalCollection(SignalLight(redLampRelay), SignalLight(redPigearRelay))
        green = None
        signals = SignalBoard(red, green)

        signals.red.pigear.on()
        self.assertEquals(signals.red.state(), SignalState.pigearOnly)
        self.assertEquals(redPigearRelay.state(), RelayState.on)
        self.assertEquals(redLampRelay.state(), RelayState.off)

    def testWhenGreenSignalIsOff_allGreenLightsCanBeTurnedOn(self):
        greenLampRelay = MockRelay()
        greenPigearRelay = MockRelay()
        red = None
        green = SignalCollection(SignalLight(greenLampRelay), SignalLight(greenPigearRelay))
        signals = SignalBoard(red, green)
        self.assertEquals(signals.green.state(), SignalState.off)

        signals.green.on()
        self.assertEquals(signals.green.state(), SignalState.on)

    def testWhenGreenSignalIsOn_allGreenLightsCanBeTurnedOff(self):
        greenLampRelay = MockRelay()
        greenPigearRelay = MockRelay()
        red = None
        green = SignalCollection(SignalLight(greenLampRelay), SignalLight(greenPigearRelay))
        signals = SignalBoard(red, green)

        signals.green.on()
        self.assertEquals(signals.green.state(), SignalState.on)

        signals.green.off()
        self.assertEquals(signals.green.state(), SignalState.off)

    def testWhenGreenSignalsAreOff_greenLampOnlyCanBeTurnedOn(self):
        greenLampRelay = MockRelay()
        greenPigearRelay = MockRelay()
        red = None
        green = SignalCollection(SignalLight(greenLampRelay), SignalLight(greenPigearRelay))
        signals = SignalBoard(red, green)

        signals.green.lamp.on()
        self.assertEquals(signals.green.state(), SignalState.lampOnly)

    def testWhenGreenSignalsAreOff_greenPigearOnlyCanBeTurnedOn(self):
        greenLampRelay = MockRelay()
        greenPigearRelay = MockRelay()
        red = None
        green = SignalCollection(SignalLight(greenLampRelay), SignalLight(greenPigearRelay))
        signals = SignalBoard(red, green)

        signals.green.pigear.on()
        self.assertEquals(signals.green.state(), SignalState.pigearOnly)

    def testWhenTurningOnGreenLamp_redLightsStayOff(self):
        greenLampRelay = MockRelay()
        greenPigearRelay = MockRelay()
        redLampRelay = MockRelay()
        redPigearRelay = MockRelay()

        red = SignalCollection(SignalLight(redLampRelay), SignalLight(redPigearRelay))
        green = SignalCollection(SignalLight(greenLampRelay), SignalLight(greenPigearRelay))

        signals = SignalBoard(red, green)

        signals.green.on()
        self.assertEquals(signals.green.state(), SignalState.on)
        self.assertEquals(signals.red.state(), SignalState.off)

    def testWhenTurningOnRedLamp_greenLightsStayOff(self):
        greenLampRelay = MockRelay()
        greenPigearRelay = MockRelay()
        redLampRelay = MockRelay()
        redPigearRelay = MockRelay()

        red = SignalCollection(SignalLight(redLampRelay), SignalLight(redPigearRelay))
        green = SignalCollection(SignalLight(greenLampRelay), SignalLight(greenPigearRelay))

        signals = SignalBoard(red, green)

        signals.red.on()
        self.assertEquals(signals.red.state(), SignalState.on)
        self.assertEquals(signals.green.state(), SignalState.off)

    def testWhenTurningOffOneLamp_bothLampsAreOff(self):
        greenLampRelay = MockRelay()
        greenPigearRelay = MockRelay()
        redLampRelay = MockRelay()
        redPigearRelay = MockRelay()

        red = SignalCollection(SignalLight(redLampRelay), SignalLight(redPigearRelay))
        green = SignalCollection(SignalLight(greenLampRelay), SignalLight(greenPigearRelay))

        signals = SignalBoard(red, green)

        signals.red.on()
        self.assertEquals(signals.red.state(), SignalState.on)
        self.assertEquals(signals.green.state(), SignalState.off)

        signals.red.off()
        self.assertEquals(signals.red.state(), SignalState.off)
        self.assertEquals(signals.green.state(), SignalState.off)




def main():
    unittest.main()

if __name__ == '__main__':
    main()