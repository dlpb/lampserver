import json

from signalboard import SignalBoard
from signalstate import SignalColour, SignalState


class SignalAPI:

    signals = None

    def __init__(self, signals):
        self.signals = signals

    def json(self, target=None):
        if target == SignalColour.red:
            signal = self.signals.red
            return json.dumps({
                'colour': 'red',
                'state': signal.state().name,
                'hypermedia': ['/api']
            })
        elif target == SignalColour.green:
            signal = self.signals.green
            return json.dumps({
                'colour': 'green',
                'state': signal.state().name,
                'hypermedia': ['/api']
            })
        else:
            return json.dumps({
                'name': self.signals.name,
                'red': {
                    'state': self.signals.red.state().name
                },
                'green': {
                    'state': self.signals.green.state().name
                },
                'hypermedia': ['/api', 'red', 'green']
            })

    def set(self, target, state):

        self.signals.red.off()
        self.signals.green.off()

        if target == SignalColour.red:
            if state == SignalState.on:
                self.signals.red.on()
            elif state == SignalState.off:
                self.signals.red.off()

        elif target == SignalColour.green:
            if state == SignalState.on:
                self.signals.green.on()
            elif state == SignalState.off:
                self.signals.green.off()


