from unittest import mock

from battleship.logic import Game, Grid
from battleship.logic.constants import Peg, column_mapping, row_mapping


def test_game_initialization():
    assert isinstance(Game(), Game)


def describe_game_creates_grids():
    with mock.patch("battleship.logic.game.Player", return_value="testing"):
        game = Game()

        def test_game_creates_player1():
            assert game.player1 == "testing"

        def test_game_creates_player2():
            assert game.player2 == "testing"


def describe_check_shot_status():
    with mock.patch("battleship.logic.game.Player", return_value="testing") as player:
        player.ocean_grid = Grid()
        player.ocean_grid.matrix[column_mapping["B"]][row_mapping["2"]] = 2
        game = Game()
        game.opponent = player

        def test_shot_is_a_hit():
            assert game.check_shot_status(("B", "2")) is True

        def test_shot_is_a_miss():
            assert game.check_shot_status(("B", "3")) is False


def describe_place_peg_current_players_target_grid():
    def place_red_peg():
        game = Game()
        game.check_shot_status = mock.MagicMock(return_value=True)
        game.place_peg(("C", "5"))
        assert game.current_player.target_grid.matrix[column_mapping["C"]][row_mapping["5"]] == Peg.RED

    def place_white_peg():
        game = Game()
        game.check_shot_status = mock.MagicMock(return_value=False)
        game.place_peg(("A", "1"))
        assert game.current_player.target_grid.matrix[column_mapping["A"]][row_mapping["1"]] == Peg.WHITE


def test_place_red_peg_opponents_ocean_grid():
    game = Game()
    game.check_shot_status = mock.MagicMock(return_value=True)
    game.place_peg(("C", "5"))
    assert game.opponent.ocean_grid.matrix[column_mapping["C"]][row_mapping["5"]] == Peg.RED
