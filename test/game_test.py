import numpy as np

from battleship.logic.game import initialise_game


def describe_initialize_boards():
    def test_player1_own_board():
        game = initialise_game()
        assert (game["player1"]["own_board"] == np.zeros((10, 10), dtype=int)).all()

    def test_player2_own_board():
        game = initialise_game()
        assert (game["player2"]["own_board"] == np.zeros((10, 10), dtype=int)).all()

    def test_player1_shots_board():
        game = initialise_game()
        assert (game["player1"]["shots_board"] == np.zeros((10, 10), dtype=int)).all()

    def test_player2_shots_board():
        game = initialise_game()
        assert (game["player2"]["shots_board"] == np.zeros((10, 10), dtype=int)).all()
