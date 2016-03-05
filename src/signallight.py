class SignalLight:

    relay = None

    def __init__(self, relay):
        self.relay = relay

    def state(self):
        return self.relay.state()

    def on(self):
        self.relay.on()

    def off(self):
        self.relay.off()
