from enum import Enum, unique, auto


@unique
class Website(Enum):
    FILIMO = auto()
    NAMAVA = auto()
    FILMNET = auto()
