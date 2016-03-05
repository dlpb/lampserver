import json
import unittest

from api import SignalAPI
from mockrelay import *


# Here's our "unit tests".
from signalboard import SignalBoard
from signalstate import SignalColour


class RelayBoardTests(unittest.TestCase):

    def test_givenASignalAPIWithAnOffSignal_itCanReturnJsonWithTheStateOfTheSignal(self):
        resource = SignalAPI(SignalBoard(MockRelay(), MockRelay()))

        expected = json.dumps({
            'red': { 'state': 'off'},
            'green': { 'state': 'off'},
            'hypermedia': ['/api', 'red', 'green']

        })

        self.assertEqual(resource.json(), expected)

    def test_givenASignalAPI_whenTurningOnRedSignal_jsonIsUpdated(self):
        signals = SignalBoard(MockRelay(), MockRelay())
        resource = SignalAPI(signals)

        signals.red.on()

        expected = json.dumps({
            'red': { 'state': 'on'},
            'green': { 'state': 'off'},
            'hypermedia': ['/api', 'red', 'green']

        })

        self.assertEqual(resource.json(), expected)

    def test_givenASignalAPI_whenTurningOnGreenSignal_jsonIsUpdated(self):
        signals = SignalBoard(MockRelay(), MockRelay())
        resource = SignalAPI(signals)

        signals.green.on()

        expected = json.dumps({
            'red': { 'state': 'off'},
            'green': { 'state': 'on'},
            'hypermedia': ['/api', 'red', 'green']
        })

        self.assertEqual(resource.json(), expected)

    def test_whenReturningJsonForSignals_hypermediaIsIncluded(self):
        signals = SignalBoard(MockRelay(), MockRelay())
        resource = SignalAPI(signals)

        expected = """"hypermedia": ["/api", "red", "green"]"""

        self.assertTrue(resource.json().__contains__(expected))

    def test_whenReturningJsonForOneSignal_jsonIsReturned(self):
        signals = SignalBoard(MockRelay(), MockRelay())
        resource = SignalAPI(signals)

        expected = """{"colour": "red", "state": "on"}"""

        self.assertTrue(resource.json(SignalColour.red).__contains__(expected))

def main():
    unittest.main()

if __name__ == '__main__':
    main()