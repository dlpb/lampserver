from main.python.relaystate import RelayState


class Relay:

    __state__ = RelayState.off

    def on(self):
        self.__state__ = RelayState.on

    def off(self):
        self.__state__ = RelayState.off

    def state(self):
        return self.__state__