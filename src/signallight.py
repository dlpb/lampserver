from relaystate import RelayState
from signalstate import SignalState


class SignalLight:

    relay = None
    colour = None

    def __init__(self, colour, relay):
        self.colour = colour
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
