from enum import Enum, IntEnum


class Peg(IntEnum):
    WHITE = 1
    RED = -1


column_mapping = {
    "A": 0,
    "B": 1,
    "C": 2,
    "D": 3,
    "E": 4,
    "F": 5,
    "G": 6,
    "H": 7,
    "I": 8,
    "J": 9,
}

row_mapping = {str(i + 1): i for i in range(10)}


class VesselIdentifier(IntEnum):
    CARRIER = 9
    BATTLESHIP = 8
    CRUISER = 7
    SUBMARINE = 6
    DESTROYER = 5


class VesselLength(IntEnum):
    CARRIER = 5
    BATTLESHIP = 4
    CRUISER = 3
    SUBMARINE = 3
    DESTROYER = 2


class Vessel(Enum):
    CARRIER = "CARRIER"
    BATTLESHIP = "BATTLESHIP"
    CRUISER = "CRUISER"
    SUBMARINE = "SUBMARINE"
    DESTROYER = "DESTROYER"


class GameStatus(IntEnum):
    PLAYER_1_WON = 1
