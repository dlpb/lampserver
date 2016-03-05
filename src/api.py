import json

from signalboard import SignalBoard

class SignalAPI:

    signals = None

    def __init__(self, signals):
        self.signals = signals

    def json(self):
        return json.dumps({
            'red': {
                'state': self.signals.red.state().name
            },
            'green': {
                'state': self.signals.green.state().name
            },
            'hypermedia': ['/api', 'red', 'green']
        })
