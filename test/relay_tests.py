import unittest
from relayboard import *
from mockrelay import *


# Here's our "unit tests".
class RelayBoardTests(unittest.TestCase):

    def testWhenCreatingNewRelayOne_stateIsOff(self):
        relay = RelayBoard(MockRelay(), MockRelay(), MockRelay(), MockRelay())
        self.assertEqual(relay.one.state(), RelayState.off)

    def test_GivenNewRelayOne_whenTurningOn_relayIsOn(self):
        relay = RelayBoard(MockRelay(), MockRelay(), MockRelay(), MockRelay())
        relay.one.on()
        self.assertEqual(relay.one.state(), RelayState.on)

    def test_GivenNewRelayOneWhichIsOn_whenTurningOff_relayIsOff(self):
        relay = RelayBoard(MockRelay(), MockRelay(), MockRelay(), MockRelay())
        relay.one.on()
        self.assertEqual(relay.one.state(), RelayState.on)
        relay.one.off()
        self.assertEqual(relay.one.state(), RelayState.off)

    def testWhenCreatingNewRelayTwo_stateIsOff(self):
        relay = RelayBoard(MockRelay(), MockRelay(), MockRelay(), MockRelay())
        self.assertEqual(relay.two.state(), RelayState.off)

    def test_GivenNewRelayTwo_whenTurningOn_relayIsOn(self):
        relay = RelayBoard(MockRelay(), MockRelay(), MockRelay(), MockRelay())
        relay.two.on()
        self.assertEqual(relay.two.state(), RelayState.on)

    def test_GivenNewRelayTwoWhichIsOn_whenTurningOff_relayIsOff(self):
        relay = RelayBoard(MockRelay(), MockRelay(), MockRelay(), MockRelay())
        relay.two.on()
        self.assertEqual(relay.two.state(), RelayState.on)
        relay.two.off()
        self.assertEqual(relay.two.state(), RelayState.off)

    def testWhenCreatingNewRelayThree_stateIsOff(self):
        relay = RelayBoard(MockRelay(), MockRelay(), MockRelay(), MockRelay())
        self.assertEqual(relay.three.state(), RelayState.off)

    def test_GivenNewRelayThree_whenTurningOn_relayIsOn(self):
        relay = RelayBoard(MockRelay(), MockRelay(), MockRelay(), MockRelay())
        relay.three.on()
        self.assertEqual(relay.three.state(), RelayState.on)

    def test_GivenNewRelayThreeWhichIsOn_whenTurningOff_relayIsOff(self):
        relay = RelayBoard(MockRelay(), MockRelay(), MockRelay(), MockRelay())
        relay.three.on()
        self.assertEqual(relay.three.state(), RelayState.on)
        relay.three.off()
        self.assertEqual(relay.three.state(), RelayState.off)

    def testWhenCreatingNewRelayFour_stateIsOff(self):
        relay = RelayBoard(MockRelay(), MockRelay(), MockRelay(), MockRelay())
        self.assertEqual(relay.four.state(), RelayState.off)

    def test_GivenNewRelayFour_whenTurningOn_relayIsOn(self):
        relay = RelayBoard(MockRelay(), MockRelay(), MockRelay(), MockRelay())
        relay.four.on()
        self.assertEqual(relay.four.state(), RelayState.on)

    def test_GivenNewRelayFourWhichIsOn_whenTurningOff_relayIsOff(self):
        relay = RelayBoard(MockRelay(), MockRelay(), MockRelay(), MockRelay())
        relay.four.on()
        self.assertEqual(relay.four.state(), RelayState.on)
        relay.four.off()
        self.assertEqual(relay.four.state(), RelayState.off)




def main():
    unittest.main()

if __name__ == '__main__':
    main()