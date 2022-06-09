import numpy as np


def initialise_game() -> dict:
    return {
        "player1": {
            "ocean_grid": np.zeros((10, 10), dtype=int),
            "target_grid": np.zeros((10, 10), dtype=int),
        },
        "player2": {
            "ocean_grid": np.zeros((10, 10), dtype=int),
            "target_grid": np.zeros((10, 10), dtype=int),
        },
    }
