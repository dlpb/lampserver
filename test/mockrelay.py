class MockRelay:

    __state__ = False

    def on(self):
        self.__state__ = True

    def off(self):
        self.__state__ = False

    def state(self):
        return self.__state__
