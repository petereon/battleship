from enum import Enum, IntEnum

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


class VesselLength(IntEnum):
    CARRIER = 5


class Vessel(Enum):
    CARRIER = "CARRIER"
    BATTLESHIP = "BATTLESHIP"
