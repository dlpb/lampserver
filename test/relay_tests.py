import unittest




class MockRelay:

    __state__ = False

    def on(self):
        self.__state__ = True

    def state(self):
        return self.__state__


class RelayBoard:

    one = MockRelay()

    # def blah(self):
    #     return False


# Here's our "unit tests".
class RelayBoardTests(unittest.TestCase):

    def testWhenCreatingNewRelayOne_stateIsOff(self):
        relay = RelayBoard()
        self.assertFalse(relay.one.state())

    def test_GivenNewRelayOne_whenTurningOn_relayIsOn(self):
        relay = RelayBoard()
        relay.one.on()
        self.assertTrue(relay.one.state())


def main():
    unittest.main()

if __name__ == '__main__':
    main()