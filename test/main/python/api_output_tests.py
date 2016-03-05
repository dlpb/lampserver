import unittest

from api import SignalAPI
from mockrelay import *
from relayboard import *


# Here's our "unit tests".
from signalboard import SignalBoard


class RelayBoardTests(unittest.TestCase):

    def test_givenASignalAPI_itCanReturnJson(self):
        resource = SignalAPI()

        expected = """{
            'state':'off'
        }"""
        self.assertEqual(resource.json(), expected)




def main():
    unittest.main()

if __name__ == '__main__':
    main()