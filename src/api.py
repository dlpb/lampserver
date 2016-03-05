from signalboard import SignalBoard

class SignalAPI:

    signals = None

    def __init__(self, signals):
        self.signals = signals

    def json(self):
        return """{
            'red':{
                'state':'off'
            },
            'green':{
                'state':'off'
            }
        }"""