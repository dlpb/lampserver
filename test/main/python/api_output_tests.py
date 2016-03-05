import unittest

from api import SignalAPI
from mockrelay import *


# Here's our "unit tests".
from signalboard import SignalBoard


class RelayBoardTests(unittest.TestCase):

    def test_givenASignalAPIWithAnOffSignal_itCanReturnJsonWithTheStateOfTheSignal(self):
        resource = SignalAPI(SignalBoard(MockRelay(), MockRelay()))

        expected = """{
            'red':{
                'state':'off'
            },
            'green':{
                'state':'off'
            }
        }"""

        self.assertEqual(resource.json(), expected)


def main():
    unittest.main()

if __name__ == '__main__':
    main()