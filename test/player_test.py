from unittest import mock

from battleship.logic import Grid, Player
from battleship.logic.constants import Peg, column_mapping, row_mapping


def describe_player():
    with mock.patch("battleship.logic.player.Grid", return_value="testing"):
        player = Player()

        def test_player_has_ocean_grid():
            assert player.ocean_grid == "testing"

        def test_player_has_target_grid():
            assert player.target_grid == "testing"


def describe_is_hole_available():
    def test_shot_available_at_A1():
        player = Player()
        assert player.is_hole_available(("A", "1")) is True

    def test_shot_taken_by_white_peg_at_C5():
        player = Player()
        player.target_grid.matrix[column_mapping["C"]][row_mapping["5"]] = Peg.WHITE
        assert player.is_hole_available(("C", "5")) is False
