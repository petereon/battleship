from unittest import mock

from battleship.logic import Grid, Player


def describe_player():
    with mock.patch("battleship.logic.player.Grid", return_value="testing"):
        player = Player()

        def test_player_has_ocean_grid():
            assert player.ocean_grid == "testing"

        def test_player_has_target_grid():
            assert player.target_grid == "testing"
