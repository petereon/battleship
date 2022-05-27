from minesweeper.logic.game import initialise_game


def test_intialise_game():
    assert initialise_game() == {
        "player1": {
            "own_board": [[], [], [], [], [], [], [], [], [], []],
            "shots_board": [[], [], [], [], [], [], [], [], [], []],
        },
        "player2": {
            "own_board": [[], [], [], [], [], [], [], [], [], []],
            "shots_board": [[], [], [], [], [], [], [], [], [], []],
        },
    }
