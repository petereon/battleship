from unittest import mock

from battleship.logic import Grid, Player

# from test.player_test import MockGrid


def describe_player():
    def test_player_has_ocean_grid():
        with mock.patch("battleship.logic.player.Grid") as MockedGrid:
            MockedGrid.return_value = "testing"
            player = Player()
            # assert isinstance(player.ocean_grid, MockedGrid)
            assert player.ocean_grid == "testing"
            # assert type(player.ocean_grid) == type(MockedGrid)

    def test_player_has_target_grid():
        with mock.patch("battleship.logic.player.Grid") as MockedGrid:
            MockedGrid.return_value = "testing"
            player = Player()
            # assert isinstance(player.ocean_grid, MockedGrid)
            assert player.target_grid == "testing"
