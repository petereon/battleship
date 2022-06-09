import numpy as np

from battleship.logic.game import initialise_game


def describe_initialize_boards():
    def test_player1_ocean_grid():
        game = initialise_game()
        assert (game["player1"]["ocean_grid"] == np.zeros((10, 10), dtype=int)).all()

    def test_player2_ocean_grid():
        game = initialise_game()
        assert (game["player2"]["ocean_grid"] == np.zeros((10, 10), dtype=int)).all()

    def test_player1_target_grid():
        game = initialise_game()
        assert (game["player1"]["target_grid"] == np.zeros((10, 10), dtype=int)).all()

    def test_player2_target_grid():
        game = initialise_game()
        assert (game["player2"]["target_grid"] == np.zeros((10, 10), dtype=int)).all()
