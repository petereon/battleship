import numpy as np
import pytest
from pytest_bdd import exceptions, given, parsers, scenario, scenarios, then, when

from battleship.logic.constants import (
    Vessel,
    VesselIdentifier,
    VesselLength,
    column_mapping,
    row_mapping,
)
from battleship.logic.player import Player, PositionError

scenarios("../features/ship_placement.feature")


@given("a player", target_fixture="player")
def given_a_player():
    return Player()


@given("the player's grids are set up")
def given_players_grids_are_set_up():
    pass


@when(parsers.parse("the player places the {vessel_type} on their ocean grid"), target_fixture="vessel_type")
def when_the_player_places_the_vessel(vessel_type):
    return vessel_type.upper()


def get_position_coordinates(position):
    start, end = position.split(", ")
    start_column, start_row = start.split(" ")
    end_column, end_row = end.split(" ")
    return ((start_column, start_row), (end_column, end_row))


@when(parsers.parse("chooses the position {position}"))
def when_the_player_chooses_the_position(position, player, vessel_type):
    player.place_vessel(Vessel[vessel_type], get_position_coordinates(position))


@when(parsers.parse("chooses an invalid position {position}"), target_fixture="error_details")
def when_the_player_chooses_an_invalid_position(position, player, vessel_type):
    with pytest.raises(PositionError) as exception_info:
        scenario("../features/ship_placement.feature", "Placing a destroyer in an invalid position")
        player.place_vessel(Vessel[vessel_type], get_position_coordinates(position))
    return exception_info


@then(parsers.parse("the {vessel_type} in position {position} on the ocean grid"))
def then_the_vessel_is_in_position(position, player, vessel_type):
    (start_column, start_row), (end_column, end_row) = get_position_coordinates(position)

    assert player.ocean_grid.matrix[column_mapping[start_column]][row_mapping[start_row]] == VesselIdentifier[vessel_type.upper()]
    assert player.ocean_grid.matrix[column_mapping[end_column]][row_mapping[end_row]] == VesselIdentifier[vessel_type.upper()]


@then(parsers.parse("the {vessel_type} has {number_of_holes:d} holes"))
def then_the_vessel_has_specified_number_of_holes(player, number_of_holes, vessel_type):
    indices = np.argwhere(player.ocean_grid.matrix == VesselIdentifier[vessel_type.upper()])
    assert len(indices) == number_of_holes


def is_straight_line(indices, vessel_type):
    cols, rows = list(zip(*indices))

    for i in range(10):

        # Vertical
        if cols.count(i) == VesselLength[vessel_type]:
            return True

        # Horizontal
        if rows.count(i) == VesselLength[vessel_type]:
            return True
    return False


@then("they are in a straight line")
def then_they_are_in_a_straight_line(player, vessel_type):
    indices = np.argwhere(player.ocean_grid.matrix == VesselIdentifier[vessel_type.upper()])
    assert is_straight_line(indices, vessel_type.upper())


@then("the player receives an error message")
def then_the_player_received_an_error_message(error_details):
    assert str(error_details.value) == "Invalid position"


@then("there is no change to their ocean grid")
def then_there_is_no_change_to_their_ocean_grid():
    pass
