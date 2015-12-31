from enum import Enum


class SignalState(Enum):
    off = 1
    lampOnly = 2
    pigearOnly = 4
    on = 8