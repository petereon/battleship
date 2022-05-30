def initialise_game() -> dict:
    return {
        "player1": {
            "own_board": [[], [], [], [], [], [], [], [], [], []],
            "shots_board": [[], [], [], [], [], [], [], [], [], []],
        },
        "player2": {
            "own_board": [[], [], [], [], [], [], [], [], [], []],
            "shots_board": [[], [], [], [], [], [], [], [], [], []],
        },
    }
