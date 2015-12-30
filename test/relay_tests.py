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

    def __init__(self, relayOne):
        self.one = relayOne

    # def blah(self):
    #     return False


# Here's our "unit tests".
class RelayBoardTests(unittest.TestCase):

    def testWhenCreatingNewRelayOne_stateIsOff(self):
        relay = RelayBoard(MockRelay())
        self.assertFalse(relay.one.state())

    def test_GivenNewRelayOne_whenTurningOn_relayIsOn(self):
        relay = RelayBoard(MockRelay())
        relay.one.on()
        self.assertTrue(relay.one.state())

    def test_GivenNewRelayOneWhichIsOn_whenTurningOff_relayIsOff(self):
        relay = RelayBoard(MockRelay())
        relay.one.on()
        self.assertTrue(relay.one.state())
        relay.one.off()
        self.assertFalse(relay.one.state())


def main():
    unittest.main()

if __name__ == '__main__':
    main()