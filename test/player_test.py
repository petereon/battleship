from unittest import mock

import numpy as np
import pytest

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


def describe_taking_a_shot():
    player = Player()

    @pytest.mark.parametrize("coord", [("C", "5"), ("A", "1"), ("J", "3")])
    def test_take_shot(coord):
        player.take_shot(coord)

        assert player.current_shot == (column_mapping[coord[0]], row_mapping[coord[1]])


@pytest.mark.parametrize(
    "sunk_vessel_indicator_state",
    [
        [0, 0, 0, 0, 0],
        [Peg.RED, 0, 0, 0, 0],
        [Peg.RED, Peg.RED, 0, 0, 0],
        [Peg.RED, Peg.RED, Peg.RED, 0, 0],
        [Peg.RED, Peg.RED, Peg.RED, Peg.RED, 0],
        [Peg.RED, Peg.RED, Peg.RED, Peg.RED, Peg.RED],
    ],
)
def test_game_starts_with_5_empty_indicators(sunk_vessel_indicator_state):
    player = Player()
    player.sunk_vessel_indicator = np.array(sunk_vessel_indicator_state)
    assert (player.check_sunk_vessel_indicator() == np.array(sunk_vessel_indicator_state)).all()
