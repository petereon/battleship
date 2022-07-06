from enum import Enum

import numpy as np
import pytest

from battleship.logic.constants import (
    Vessel,
    VesselIdentifier,
    column_mapping,
    row_mapping,
)
from battleship.logic.player import Player


@pytest.fixture
def get_player():
    return Player()


def describe_placing_ship():
    def place_horizontal_carrier_on_C5_C9_start_hole_test(get_player):
        player = get_player
        player.place_vessel(Vessel.CARRIER, (("C", "5"), ("C", "9")))
        assert player.ocean_grid.matrix[column_mapping["C"]][row_mapping["5"]] == VesselIdentifier["CARRIER"]

    def place_horizontal_carrier_on_C5_C9_end_hole_test(get_player):
        player = get_player
        player.place_vessel(Vessel.CARRIER, (("C", "5"), ("C", "9")))
        assert player.ocean_grid.matrix[column_mapping["C"]][row_mapping["9"]] == VesselIdentifier["CARRIER"]

    def place_horizontal_carrier_on_C5_C9_length_is_5_test(get_player):
        player = get_player
        player.place_vessel(Vessel.CARRIER, (("C", "5"), ("C", "9")))
        indices = np.argwhere(player.ocean_grid.matrix == VesselIdentifier["CARRIER"])
        assert len(indices) == 5

    def place_horizontal_carrier_on_B2_B6_shape_is_5_test(get_player):
        player = get_player
        player.place_vessel(Vessel.CARRIER, (("B", "2"), ("B", "6")))
        indices = np.argwhere(player.ocean_grid.matrix == VesselIdentifier["CARRIER"])
        expected = np.array(
            [
                [column_mapping["B"], row_mapping["2"]],
                [column_mapping["B"], row_mapping["3"]],
                [column_mapping["B"], row_mapping["4"]],
                [column_mapping["B"], row_mapping["5"]],
                [column_mapping["B"], row_mapping["6"]],
            ],
        )
        np.testing.assert_array_equal(indices, expected)

    def place_vertical_carrier_on_C5_C9_shape_is_5_test(get_player):
        player = get_player
        player.place_vessel(Vessel.CARRIER, (("C", "5"), ("G", "5")))
        indices = np.argwhere(player.ocean_grid.matrix == VesselIdentifier["CARRIER"])
        expected = np.array(
            [
                [column_mapping["C"], row_mapping["5"]],
                [column_mapping["D"], row_mapping["5"]],
                [column_mapping["E"], row_mapping["5"]],
                [column_mapping["F"], row_mapping["5"]],
                [column_mapping["G"], row_mapping["5"]],
            ],
        )
        np.testing.assert_array_equal(indices, expected)

    def place_horizontal_battleship_on_C5_C8_start_hole_test(get_player):
        player = get_player
        player.place_vessel(Vessel.BATTLESHIP, (("C", "5"), ("C", "8")))
        assert player.ocean_grid.matrix[column_mapping["C"]][row_mapping["5"]] == VesselIdentifier["BATTLESHIP"]

    def place_horizontal_battleship_on_B2_B5_shape_is_4_test(get_player):
        player = get_player
        player.place_vessel(Vessel.BATTLESHIP, (("B", "2"), ("B", "5")))
        indices = np.argwhere(player.ocean_grid.matrix == VesselIdentifier["BATTLESHIP"])
        expected = np.array(
            [
                [column_mapping["B"], row_mapping["2"]],
                [column_mapping["B"], row_mapping["3"]],
                [column_mapping["B"], row_mapping["4"]],
                [column_mapping["B"], row_mapping["5"]],
            ],
        )
        np.testing.assert_array_equal(indices, expected)

    def place_horizontal_cruiser_on_B2_D2_shape_is_3_test(get_player):
        player = get_player
        player.place_vessel(Vessel.CRUISER, (("B", "2"), ("D", "2")))
        indices = np.argwhere(player.ocean_grid.matrix == VesselIdentifier["CRUISER"])
        expected = np.array(
            [
                [column_mapping["B"], row_mapping["2"]],
                [column_mapping["C"], row_mapping["2"]],
                [column_mapping["D"], row_mapping["2"]],
            ],
        )
        np.testing.assert_array_equal(indices, expected)

    def place_vertical_cruiser_on_G4_G6_shape_is_3_test(get_player):
        player = get_player
        player.place_vessel(Vessel.CRUISER, (("G", "4"), ("G", "6")))
        indices = np.argwhere(player.ocean_grid.matrix == VesselIdentifier["CRUISER"])
        expected = np.array(
            [
                [column_mapping["G"], row_mapping["4"]],
                [column_mapping["G"], row_mapping["5"]],
                [column_mapping["G"], row_mapping["6"]],
            ],
        )
        np.testing.assert_array_equal(indices, expected)

    def place_vertical_submarine_on_G3_G5_shape_is_3_test(get_player):
        player = get_player
        player.place_vessel(Vessel.SUBMARINE, (("G", "3"), ("G", "5")))
        indices = np.argwhere(player.ocean_grid.matrix == VesselIdentifier["SUBMARINE"])
        expected = np.array(
            [
                [column_mapping["G"], row_mapping["3"]],
                [column_mapping["G"], row_mapping["4"]],
                [column_mapping["G"], row_mapping["5"]],
            ],
        )
        np.testing.assert_array_equal(indices, expected)
