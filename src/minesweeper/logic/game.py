import numpy as np


def initialise_game() -> dict:
    return {
        "player1": {
            "own_board": np.zeros((10, 10), dtype=int),
            "shots_board": np.zeros((10, 10), dtype=int),
        },
        "player2": {
            "own_board": np.zeros((10, 10), dtype=int),
            "shots_board": np.zeros((10, 10), dtype=int),
        },
    }
