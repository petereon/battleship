from unittest import mock

from battleship.logic import Grid, Player

# from test.player_test import MockGrid


def test_player_has_ocean_grid():
    with mock.patch("battleship.logic.Grid", autospec=True) as MockedGrid:
        MockedGrid.return_value = "testing"
        blah = MockedGrid()
        print("BLAH", blah)
        player = Player()
        print("!!!", Grid())
        print("GRID", player.ocean_grid)
        # assert isinstance(player.ocean_grid, type(MockGrid))
        assert player.ocean_grid is MockedGrid
        # assert type(player.ocean_grid) == type(MockGrid)

    # def test_player_has_target_grid():
    #     with mock.patch("battleship.logic.Grid", mock.MagicMock):
    #         player = Player()

    #         assert isinstance(player.target_grid, mock.MagicMock)
