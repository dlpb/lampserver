import unittest


class Signal:
    relay = None

    def __init__(self, relay):
        self.relay = relay

    def state(self):
        return False



class SignalCollection:

    lamp = None
    pigear = None

    def __init__(self, lamp, pigear):
        self.lamp = lamp
        self.pigear = pigear

    def state(self):
        return self.lamp.state() and self.pigear.state()


class SignalBoard:
    red = None
    green = None

    def __init__(self, red, green):
        self.red = red
        self.green = green


class SignalBoardTests(unittest.TestCase):

    def testWhenCreatingSignalBoard_redLightsAreOff(self):

        red = SignalCollection(Signal(None), Signal(None))
        green = SignalCollection(Signal(None), Signal(None))
        signals = SignalBoard(red, green)
        self.assertFalse(signals.red.state())




def main():
    unittest.main()

if __name__ == '__main__':
    main()