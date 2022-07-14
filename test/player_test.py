from unittest import mock

from battleship.logic import Grid, Player
from battleship.logic.constants import column_mapping, row_mapping


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
        assert player.is_hole_available((column_mapping["A"], row_mapping["1"])) is True
