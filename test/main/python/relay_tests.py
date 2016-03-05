import unittest

from mockrelay import *
from relayboard import *


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

    def test_whenCreatingNewRelayBoard_itInitialisesAllRelaysToOff(self):

        class RecordOffRelay:
            wasOffCalled = False

            def off(self):
                self.wasOffCalled = True

            def hasOffBeenCalled(self):
                return self.wasOffCalled

        one = RecordOffRelay()
        two = RecordOffRelay()
        three = RecordOffRelay()
        four = RecordOffRelay()

        RelayBoard(one, two, three, four)

        self.assertTrue(one.hasOffBeenCalled())
        self.assertTrue(two.hasOffBeenCalled())
        self.assertTrue(three.hasOffBeenCalled)
        self.assertTrue(four.hasOffBeenCalled())


def main():
    unittest.main()

if __name__ == '__main__':
    main()