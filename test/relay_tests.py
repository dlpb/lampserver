import unittest


class MockRelay:

    __state__ = False

    def on(self):
        self.__state__ = True

    def off(self):
        self.__state__ = False

    def state(self):
        return self.__state__


class RelayBoard:

    one = None
    two = None
    three = None
    four = None

    def __init__(self, relay_one, relay_two, relay_three, relay_four):
        self.one = relay_one
        self.two = relay_two
        self.three = relay_three
        self.four = relay_four

    # def blah(self):
    #     return False


# Here's our "unit tests".
class RelayBoardTests(unittest.TestCase):

    def testWhenCreatingNewRelayOne_stateIsOff(self):
        relay = RelayBoard(MockRelay(), MockRelay(), MockRelay(), MockRelay())
        self.assertFalse(relay.one.state())

    def test_GivenNewRelayOne_whenTurningOn_relayIsOn(self):
        relay = RelayBoard(MockRelay(), MockRelay(), MockRelay(), MockRelay())
        relay.one.on()
        self.assertTrue(relay.one.state())

    def test_GivenNewRelayOneWhichIsOn_whenTurningOff_relayIsOff(self):
        relay = RelayBoard(MockRelay(), MockRelay(), MockRelay(), MockRelay())
        relay.one.on()
        self.assertTrue(relay.one.state())
        relay.one.off()
        self.assertFalse(relay.one.state())

    def testWhenCreatingNewRelayTwo_stateIsOff(self):
        relay = RelayBoard(MockRelay(), MockRelay(), MockRelay(), MockRelay())
        self.assertFalse(relay.two.state())

    def test_GivenNewRelayTwo_whenTurningOn_relayIsOn(self):
        relay = RelayBoard(MockRelay(), MockRelay(), MockRelay(), MockRelay())
        relay.two.on()
        self.assertTrue(relay.two.state())

    def test_GivenNewRelayTwoWhichIsOn_whenTurningOff_relayIsOff(self):
        relay = RelayBoard(MockRelay(), MockRelay(), MockRelay(), MockRelay())
        relay.two.on()
        self.assertTrue(relay.two.state())
        relay.two.off()
        self.assertFalse(relay.two.state())

    def testWhenCreatingNewRelayThree_stateIsOff(self):
        relay = RelayBoard(MockRelay(), MockRelay(), MockRelay(), MockRelay())
        self.assertFalse(relay.three.state())

    def test_GivenNewRelayThree_whenTurningOn_relayIsOn(self):
        relay = RelayBoard(MockRelay(), MockRelay(), MockRelay(), MockRelay())
        relay.three.on()
        self.assertTrue(relay.three.state())

    def test_GivenNewRelayThreeWhichIsOn_whenTurningOff_relayIsOff(self):
        relay = RelayBoard(MockRelay(), MockRelay(), MockRelay(), MockRelay())
        relay.three.on()
        self.assertTrue(relay.three.state())
        relay.three.off()
        self.assertFalse(relay.three.state())

    def testWhenCreatingNewRelayFour_stateIsOff(self):
        relay = RelayBoard(MockRelay(), MockRelay(), MockRelay(), MockRelay())
        self.assertFalse(relay.four.state())

    def test_GivenNewRelayFour_whenTurningOn_relayIsOn(self):
        relay = RelayBoard(MockRelay(), MockRelay(), MockRelay(), MockRelay())
        relay.four.on()
        self.assertTrue(relay.four.state())

    def test_GivenNewRelayFourWhichIsOn_whenTurningOff_relayIsOff(self):
        relay = RelayBoard(MockRelay(), MockRelay(), MockRelay(), MockRelay())
        relay.four.on()
        self.assertTrue(relay.four.state())
        relay.four.off()
        self.assertFalse(relay.four.state())




def main():
    unittest.main()

if __name__ == '__main__':
    main()