import json

from signalboard import SignalBoard
from signalstate import SignalColour, SignalState


class SignalAPI:

    signals = None

    def __init__(self, signals):
        self.signals = signals

    def json(self, target=None):
        if target == SignalColour.red:
            state = self.signals.red.state().name
            return self.single_signal_json('red', state)
        elif target == SignalColour.green:
            state = self.signals.green.state().name
            return self.single_signal_json('green', state)
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

    @staticmethod
    def single_signal_json(name, state):
        return json.dumps({
            'colour': name,
            'state': state,
            'hypermedia': ['/api']
        })

    def set(self, target, state):

        self.signals.red.off()
        self.signals.green.off()

        if state == SignalState.on:
            if target == SignalColour.red:
                self.signals.red.on()

            elif target == SignalColour.green:
                self.signals.green.on()



