class RelayBoard:

    one = None
    two = None
    three = None
    four = None

    def __init__(self, relay_one, relay_two, relay_three, relay_four):
        self.one = relay_one
        self.two = relay_two
        self.three = relay_three
        self.four = relay_four

        self.one.off()
        self.two.off()
        self.three.off()
        self.four.off()