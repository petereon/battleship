from enum import Enum

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

CARRIER = 9
CARRIER_LENGTH = 5


class Vessel(Enum):
    CARRIER = "CARRIER"
