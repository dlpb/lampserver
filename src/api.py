import json

from signalboard import SignalBoard
from signalstate import SignalColour


class SignalAPI:

    signals = None

    def __init__(self, signals):
        self.signals = signals

    def json(self, signal = None):
        if signal == SignalColour.red:
            return """{"colour": "red", "state": "on"}"""

        else:
            return json.dumps({
                'red': {
                    'state': self.signals.red.state().name
                },
                'green': {
                    'state': self.signals.green.state().name
                },
                'hypermedia': ['/api', 'red', 'green']
            })


