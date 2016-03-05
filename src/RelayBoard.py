class RelayBoard:

    one = None
    two = None

    def __init__(self, relay_one, relay_two):
        self.one = relay_one
        self.two = relay_two

        self.one.off()
        self.two.off()