import json

from twisted.internet import reactor
from twisted.web import resource
from twisted.web.resource import Resource
from twisted.web.server import Site
from twisted.web.static import File

from relay import Relay
from relaystate import RelayState
from signalboard import SignalBoard
from signalcollection import SignalCollection
from signallight import SignalLight


class SignalSummaryResources(resource.Resource):
    isLeaf = False
    signals = None

    def __init__(self, signalboard):
        Resource.__init__(self)
        self.signals = signalboard

    def render_GET(self, request):
        body = json.dumps({
            'state': {
                "red": self.signals.red.state().name,
                "green": self.signals.green.state().name
            },
            "hypermedia": ['red', 'green']
        })
        request.setHeader("content-type", "application/json")
        return body


class SignalColourResources(resource.Resource):
    isLeaf = False
    signals = None

    def __init__(self, signalcollection):
        Resource.__init__(self)
        self.signals = signalcollection

    def render_GET(self, request):
        body = json.dumps({
            'state': {
                "lamp": self.signals.lamp.state().name,
                "pigear": self.signals.pigear.state().name
            },
            "hypermedia": ['lamp', 'pigear']
        })
        request.setHeader("content-type", "application/json")
        return body

    def render_POST(self, request):

        request.setHeader("content-type", "text/plain")

        if "state" in request.args:
            state = request.args["state"][0]

            if state.lower() == "on":
                self.signals.lamp.on()
                self.signals.pigear.on()
            elif state.lower() == "off":
                self.signals.lamp.off()
                self.signals.pigear.off()
            else:
                return json.dumps({
                    "result": "error",
                    "error": {
                        "shortMessage": "Bad value for state field",
                        "detailedMessage": "An incorrect value for the state field was provided." +
                                           " Please provide a state field in post body, with vale of 'on' or 'off'"
                    }
                })
            return json.dumps({
                "result": "ok"
            })

        else:
            return json.dumps({
                "result": "error",
                "error": {
                    "shortMessage": "No state field provided",
                    "detailedMessage": "No state field was provided." +
                                       " Please provide a state field in post body, with vale of 'on' or 'off'"
                }
            })


class SignalLightResources(resource.Resource):
    isLeaf = True
    lamp = None

    def __init__(self, lamp):
        Resource.__init__(self)
        self.lamp = lamp

    def render_GET(self, request):
        body = json.dumps({
            'state': self.lamp.state().name
        })
        request.setHeader("content-type", "application/json")
        return body

    def render_POST(self, request):
        request.setHeader("content-type", "text/plain")

        if "state" in request.args:
            state = request.args["state"][0]

            if state.lower() == "on":
                self.lamp.on()
            elif state.lower() == "off":
                self.lamp.off()
            else:
                return json.dumps({
                    "result": "error",
                    "error": {
                        "shortMessage": "Bad value for state field",
                        "detailedMessage": "An incorrect value for the state field was provided." +
                                           " Please provide a state field in post body, with vale of 'on' or 'off'"
                    }
                })
            return json.dumps({
                "result": "ok"
            })

        else:
            return json.dumps({
                "result": "error",
                "error": {
                    "shortMessage": "No state field provided",
                    "detailedMessage": "No state field was provided." +
                                       " Please provide a state field in post body, with vale of 'on' or 'off'"
                }
            })


class MockRelay:

    __state__ = RelayState.off

    def __init__(self, number = 0):
        #     do nothring
        ()

    def on(self):
        self.__state__ = RelayState.on

    def off(self):
        self.__state__ = RelayState.off

    def state(self):
        return self.__state__

root = Resource()
# signals = SignalBoard(SignalCollection(SignalLight(Relay(0)), SignalLight(Relay(1))),
#                       SignalCollection(SignalLight(Relay(2)), SignalLight(Relay(3))))
signals = SignalBoard(SignalCollection(SignalLight(MockRelay(0)), SignalLight(MockRelay(1))),
                      SignalCollection(SignalLight(MockRelay(2)), SignalLight(MockRelay(3))))

signal = SignalSummaryResources(signals)
redSignal = SignalColourResources(signals.red)
greenSignal = SignalColourResources(signals.green)

signal.putChild("red", redSignal)
signal.putChild("green", greenSignal)

redSignal.putChild("lamp", SignalLightResources(signals.red.lamp))
redSignal.putChild("pigear", SignalLightResources(signals.red.pigear))

greenSignal.putChild("lamp", SignalLightResources(signals.green.lamp))
greenSignal.putChild("pigear", SignalLightResources(signals.green.pigear))

root.putChild("signal", signal)

root.putChild("", File("resources/html"))

factory = Site(root)
reactor.listenTCP(8880, factory)
reactor.run()
