import unittest


from mockrelay import MockRelay
from relaystate import RelayState
from signalboard import SignalBoard
from signallight import SignalLight
from signalstate import SignalState


class SignalBoardTests(unittest.TestCase):

    def testWhenCreatingSignalBoard_redLightsAreOff(self):
        red = SignalLight(MockRelay())
        green = None
        signals = SignalBoard(red, green)
        self.assertEqual(signals.red.state(), SignalState.off)

    def testWhenCreatingSignalBoard_greenLightsAreOff(self):
        red = None
        green = SignalLight(MockRelay())
        signals = SignalBoard(red, green)
        self.assertEquals(signals.green.state(), SignalState.off)

    def testWhenRedSignalIsOff_allRedLightsCanBeTurnedOn(self):
        redLampRelay = MockRelay()
        red = SignalLight(redLampRelay)
        green = None
        signals = SignalBoard(red, green)
        self.assertEquals(signals.red.state(), SignalState.off)
        self.assertEquals(redLampRelay.state(), RelayState.off)

        signals.red.on()
        self.assertEquals(signals.red.state(), SignalState.on)
        self.assertEquals(redLampRelay.state(), RelayState.on)

    def testWhenRedSignalIsOn_allRedLightsCanBeTurnedOff(self):
        redLampRelay = MockRelay()
        red = SignalLight(redLampRelay)
        green = None
        signals = SignalBoard(red, green)

        signals.red.on()
        self.assertEquals(signals.red.state(), SignalState.on)
        self.assertEquals(redLampRelay.state(), RelayState.on)

        signals.red.off()
        self.assertEquals(signals.red.state(), SignalState.off)
        self.assertEquals(redLampRelay.state(), RelayState.off)



    def testWhenGreenSignalIsOff_allGreenLightsCanBeTurnedOn(self):
        greenLampRelay = MockRelay()
        red = None
        green = SignalLight(greenLampRelay)
        signals = SignalBoard(red, green)
        self.assertEquals(signals.green.state(), SignalState.off)

        signals.green.on()
        self.assertEquals(signals.green.state(), SignalState.on)

    def testWhenGreenSignalIsOn_allGreenLightsCanBeTurnedOff(self):
        greenLampRelay = MockRelay()
        red = None
        green = SignalLight(greenLampRelay)
        signals = SignalBoard(red, green)

        signals.green.on()
        self.assertEquals(signals.green.state(), SignalState.on)

        signals.green.off()
        self.assertEquals(signals.green.state(), SignalState.off)

    def testWhenTurningOnGreenLamp_redLightsStayOff(self):
        greenLampRelay = MockRelay()
        redLampRelay = MockRelay()

        red = SignalLight(redLampRelay)
        green = SignalLight(greenLampRelay)

        signals = SignalBoard(red, green)

        signals.green.on()
        self.assertEquals(signals.green.state(), SignalState.on)
        self.assertEquals(signals.red.state(), SignalState.off)

    def testWhenTurningOnRedLamp_greenLightsStayOff(self):
        greenLampRelay = MockRelay()
        redLampRelay = MockRelay()

        red = SignalLight(redLampRelay)
        green = SignalLight(greenLampRelay)

        signals = SignalBoard(red, green)

        signals.red.on()
        self.assertEquals(signals.red.state(), SignalState.on)
        self.assertEquals(signals.green.state(), SignalState.off)




def main():
    unittest.main()

if __name__ == '__main__':
    main()