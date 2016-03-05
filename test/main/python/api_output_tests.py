import json
import unittest

from api import SignalAPI
from mockrelay import *


# Here's our "unit tests".
from signalboard import SignalBoard
from signallight import SignalLight
from signalstate import SignalColour, SignalState


class RelayBoardTests(unittest.TestCase):

    def testWhenGeneratingSignalAPI_JsonIncludesSignalName(self):
        resource = SignalAPI(SignalBoard(MockRelay(), MockRelay(), "SignalBoardName"))

        expected = "SignalBoardName"
        actual = decode_signal_api_response(resource.json())

        self.assertEqual(expected, actual.name)

    def test_givenASignalAPIWithAnOffSignal_itCanReturnJsonWithTheStateOfTheSignal(self):
        resource = SignalAPI(SignalBoard(SignalLight(MockRelay()), SignalLight(MockRelay())))

        actual = decode_signal_api_response(resource.json())
        self.assertEqual(actual.red, {'state': 'off'})
        self.assertEqual(actual.green, {'state': 'off'})

    def test_givenASignalAPI_whenTurningOnRedSignal_jsonIsUpdated(self):
        signals = SignalBoard(SignalLight(MockRelay()), SignalLight(MockRelay()))
        resource = SignalAPI(signals)

        signals.red.on()

        actual = decode_signal_api_response(resource.json())
        self.assertEqual(actual.red, {'state': 'on'})
        self.assertEqual(actual.green, {'state': 'off'})

    def test_givenASignalAPI_whenTurningOnGreenSignal_jsonIsUpdated(self):
        signals = SignalBoard(SignalLight(MockRelay()), SignalLight(MockRelay()))
        resource = SignalAPI(signals)

        signals.green.on()

        actual = decode_signal_api_response(resource.json())
        self.assertEqual(actual.red, {'state': 'off'})
        self.assertEqual(actual.green, {'state': 'on'})

    def test_whenReturningJsonForSignals_hypermediaIsIncluded(self):
        signals = SignalBoard(SignalLight(MockRelay()), SignalLight(MockRelay()))
        resource = SignalAPI(signals)

        expected = ["/api", "red", "green"]
        actual = decode_signal_api_response(resource.json())

        self.assertEqual(expected, actual.hypermedia)

    def test_whenReturningJsonForOneSignal_jsonIsReturned(self):
        signals = SignalBoard(SignalLight(MockRelay()), SignalLight(MockRelay()))
        resource = SignalAPI(signals)

        actual = decode_signal_api_response(resource.json(SignalColour.red))
        self.assertEqual(actual.colour, 'red')
        self.assertEqual(actual.state, 'off')


    def test_whenReturningJsonForRedSignalAndTurningItOn_correctJsonIsReturned(self):
        signals = SignalBoard(SignalLight(MockRelay()), SignalLight(MockRelay()))
        resource = SignalAPI(signals)

        signals.red.on()

        actual = decode_signal_api_response(resource.json(SignalColour.red))
        self.assertEqual(actual.colour, 'red')
        self.assertEqual(actual.state, 'on')

    def test_whenReturningJsonForGreenSignalAndTurningItOn_correctJsonIsReturned(self):
        signals = SignalBoard(SignalLight(MockRelay()), SignalLight(MockRelay()))
        resource = SignalAPI(signals)

        signals.green.on()

        actual = decode_signal_api_response(resource.json(SignalColour.green))
        self.assertEqual(actual.colour, 'green')
        self.assertEqual(actual.state, 'on')

    def test_whenReturningJsonForOneSignal_hypermediaIsIncluded(self):
        signals = SignalBoard(SignalLight(MockRelay()), SignalLight(MockRelay()))
        resource = SignalAPI(signals)

        expected = ['/api']
        actual = decode_signal_api_response(resource.json(SignalColour.red))

        self.assertEqual(expected, actual.hypermedia)

    def test_whenTurningRedLampOn_lampIsTurnedOn(self):
        signals = SignalBoard(SignalLight(MockRelay()), SignalLight(MockRelay()))
        resource = SignalAPI(signals)

        self.assertEqual(SignalState.off, signals.red.state())
        resource.set(SignalColour.red, SignalState.on)
        self.assertEqual(SignalState.on, signals.red.state())

    def test_whenTurningGreenLampOn_lampIsTurnedOn(self):
        signals = SignalBoard(SignalLight(MockRelay()), SignalLight(MockRelay()))
        resource = SignalAPI(signals)

        self.assertEqual(SignalState.off, signals.green.state())
        resource.set(SignalColour.green, SignalState.on)
        self.assertEqual(SignalState.on, signals.green.state())

    def test_whenGreenLampIsOn_itCanBeTurnedOff(self):
        signals = SignalBoard(SignalLight(MockRelay()), SignalLight(MockRelay()))
        resource = SignalAPI(signals)

        signals.green.on()
        self.assertEqual(SignalState.on, signals.green.state())

        resource.set(SignalColour.green, SignalState.off)
        self.assertEqual(SignalState.off, signals.green.state())

    def test_whenRedLampIsOn_itCanBeTurnedOff(self):
        signals = SignalBoard(SignalLight(MockRelay()), SignalLight(MockRelay()))
        resource = SignalAPI(signals)

        signals.red.on()
        self.assertEqual(SignalState.on, signals.red.state())

        resource.set(SignalColour.red, SignalState.off)
        self.assertEqual(SignalState.off, signals.red.state())

    def test_whenRedLampIsOn_whenTurningOnGreen_redIsOffAndGreenIsOn(self):
        signals = SignalBoard(SignalLight(MockRelay()), SignalLight(MockRelay()))
        resource = SignalAPI(signals)

        # given
        resource.set(SignalColour.red, SignalState.on)
        self.assertEqual(SignalState.on, signals.red.state())
        self.assertEqual(SignalState.off, signals.green.state())

        # when
        resource.set(SignalColour.green, SignalState.on)

        # then
        self.assertEqual(SignalState.off, signals.red.state())
        self.assertEqual(SignalState.on, signals.green.state())

class SignalAPIData(object):
    def __init__(self, name, red, green, hypermedia):
        self.name = name
        self.red = red
        self.green = green
        self.hypermedia = hypermedia


class SingleSignalAPIData(object):
    def __init__(self, colour, state, hypermedia):
        self.colour = colour
        self.state = state
        self.hypermedia = hypermedia


def decode_signal_api_response(response):
    data = json.loads(response)
    try:
        return SignalAPIData(**data)
    except:
        return SingleSignalAPIData(**data)


def main():
    unittest.main()

if __name__ == '__main__':
    main()