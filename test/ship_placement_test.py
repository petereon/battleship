from enum import Enum

import numpy as np
import pytest

from battleship.logic.constants import CARRIER, Vessel, column_mapping, row_mapping
from battleship.logic.player import Player


@pytest.fixture
def get_player():
    return Player()


def describe_placing_ship():
    def place_horizontal_carrier_on_C5_C9_start_hole_test(get_player):
        player = get_player
        player.place_vessel(Vessel.CARRIER.value, (("C", "5"), ("C", "9")))
        assert player.ocean_grid.matrix[column_mapping["C"]][row_mapping["5"]] == CARRIER

    def place_horizontal_carrier_on_C5_C9_end_hole_test(get_player):
        player = get_player
        player.place_vessel(Vessel.CARRIER.value, (("C", "5"), ("C", "9")))
        assert player.ocean_grid.matrix[column_mapping["C"]][row_mapping["9"]] == CARRIER

    def place_horizontal_carrer_on_C5_C9_length_is_5_test(get_player):
        player = get_player
        player.place_vessel(Vessel.CARRIER.value, (("C", "5"), ("C", "9")))
        indices = np.argwhere(player.ocean_grid.matrix == CARRIER)
        assert len(indices) == 5
