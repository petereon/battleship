import numpy as np
import pytest
from pytest_bdd import given, parsers, scenarios, then, when

from battleship.logic import Game
from battleship.logic.constants import (
    Peg,
    VesselIdentifier,
    VesselLength,
    column_mapping,
    row_mapping,
)

scenarios("../features/sunk_vessel.feature")


@pytest.fixture
def game():
    return Game()


@given(parsers.parse("I have sunk a vessel {vessel_type} starting at {start_hole}"), target_fixture="current_game")
def given_i_have_sunk_a_vessel(vessel_type, game, start_hole):
    column, row = start_hole
    length = VesselLength[vessel_type.upper()]
    for i in range(length):
        game.opponent.ocean_grid.matrix[column_mapping[column]][row_mapping[row] + i] = VesselIdentifier[vessel_type.upper()]
        game.current_player.target_grid.matrix[column_mapping[column]][row_mapping[row] + i] = Peg.RED
    return game


@given(parsers.parse("I have shot at {shot_hole}"), target_fixture="shot_hole")
def given_I_have_shot_at_shot_hole(shot_hole):
    return shot_hole


@when("the game checks the sunk vessel status", target_fixture="sunk_vessel_status")
def when_the_game_checks_the_sunk_vessel_status(current_game, shot_hole):
    column, row = shot_hole
    return current_game.check_sunk_vessel_status((column, row))


@then(parsers.parse("I know that the vessel {vessel_type} has been sunk"))
def then_i_know_that_the_vessel_has_been_sunk(sunk_vessel_status):
    assert sunk_vessel_status is True


@given("I have an empty target grid", target_fixture="target_grid")
def given_an_empty_target_grid(game):
    return game.current_player.target_grid


@when("game checks sunk vessel indicator", target_fixture="sunk_vessel_indicator")
def when_the_game_checks_sunk_vessel_indicator(game):
    return game.check_sunk_vessel_indicator()


@then("it contains 5 empty holes")
def then_it_contains_5_empty_holes(sunk_vessel_indicator):
    assert (sunk_vessel_indicator == np.zeros((5))).all()


@when("the game updates sunk vessel indicator", target_fixture="sunk_vessel_indicator")
def when_the_game_updates_sunk_vessel_indicator(current_game, shot_hole):
    column, row = shot_hole
    current_game.update_sunk_vessel_indicator((column, row))
    return current_game.check_sunk_vessel_indicator()


@then("the red peg has been added to the sunk vessel indicator")
def then_the_game_adds_a_red_peg_to_sunk_vessel_indicator(sunk_vessel_indicator):
    assert (sunk_vessel_indicator == np.ndarray([Peg.RED, 0, 0, 0, 0])).all()
