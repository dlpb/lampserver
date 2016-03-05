from relaystate import RelayState
from signalstate import SignalState


class SignalLight:

    relay = None
    name = None

    def __init__(self, name, relay):
        self.name = name
        self.relay = relay

    def state(self):
        if self.relay.state() == RelayState.off:
            return SignalState.off
        elif self.relay.state() == RelayState.on:
            return SignalState.on

    def on(self):
        self.relay.on()

    def off(self):
        self.relay.off()
