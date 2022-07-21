import pytest
from pytest_bdd import given, parsers, scenarios, then, when

from battleship.logic import Game
from battleship.logic.constants import (
    Peg,
    VesselIdentifier,
    VesselLength,
    column_mapping,
)

scenarios("../features/sunk_vessel.feature")


@pytest.fixture
def game():
    return Game()


@given(parsers.parse("I have sunk a vessel {vessel_type}"), target_fixture="current_game")
def given_i_have_sunk_a_vessel(vessel_type, game):
    length = VesselLength[vessel_type.upper()]
    for i in range(length):
        game.opponent.ocean_grid.matrix[column_mapping["A"]][i] = VesselIdentifier[vessel_type.upper()]
        game.current_player.target_grid.matrix[column_mapping["A"]][i] = Peg.RED
    return game


@when("the game checks the sunk vessel status", target_fixture="sunk_vessel_status")
def when_the_game_checks_the_sunk_vessel_status():
    return game.check_sunk_vessel_status()


@then(parsers.parse("I know that the vessel {vessel_type} has been sunk"))
def then_i_know_that_the_vessel_has_been_sunk(sunk_vessel_status):
    assert sunk_vessel_status is True
