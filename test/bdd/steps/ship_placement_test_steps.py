import numpy as np
from pytest_bdd import given, parsers, scenarios, then, when

from battleship.logic.player import Player

scenarios("../features/ship_placement.feature")


@given("a player", target_fixture="player")
def given_a_player():
    return Player()


@given("the player's grids are set up")
def given_players_grids_are_set_up():
    pass


@when("the player places the carrier on their ocean grid", target_fixture="vessel_type")
def when_the_player_places_the_carrier():
    return "carrier"


def get_position_coordinates(position):
    start, end = position.split(",")
    start_column, start_row = start.strip()
    end_column, end_row = end.strip()
    return ((start_column, start_row), (end_column, end_row))


@when(parsers.parse("chooses the position {position}"))
def when_the_player_chooses_the_position(position, player, vessel_type):
    player.place_vessel(vessel_type, get_position_coordinates(position))


column_mapping = {
    "A": 0,
    "B": 1,
    "C": 2,
    "D": 3,
    "E": 4,
    "F": 5,
    "G": 6,
    "H": 7,
    "I": 8,
    "J": 9,
}
CARRIER = 9
CARRIER_LENGTH = 5


@then(parsers.parse("the carrier in position {position} on the ocean grid"))
def then_the_carrier_is_in_position(position, player):
    (start_column, start_row), (end_column, end_row) = get_position_coordinates(position)

    assert player.ocean_grid.matrix[start_row - 1][column_mapping(start_column)] == CARRIER
    assert player.ocean_grid.matrix[end_row - 1][column_mapping(end_column)] == CARRIER


@then("the carrier has 5 holes")
def then_the_carrier_has_5_holes(player):
    indices = np.argwhere(player.ocean_grid == 9)
    assert len(indices) == 5


def is_straight_line(indices):
    cols, rows = list(zip(*indices))

    for i in range(10):

        # Vertical
        if cols.count(i) == CARRIER_LENGTH:
            return True

        # Horizontal
        if rows.count(i) == CARRIER_LENGTH:
            return True
    return False


@then("they are in a straight line")
def then_they_are_in_a_straight_line(player):
    indices = np.argwhere(player.ocean_grid == 9)
    assert is_straight_line(indices)
