import numpy as np
import pytest
from pytest_bdd import given, parsers, scenarios, then, when

from battleship.logic import Game
from battleship.logic.constants import (
    GameStatus,
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
def given_I_have_shot_at_shot_hole(shot_hole, current_game):
    current_game.current_player.current_shot = (column_mapping[shot_hole[0]], row_mapping[shot_hole[1]])
    return shot_hole


@when("the game checks the sunk vessel status", target_fixture="sunk_vessel_status")
def when_the_game_checks_the_sunk_vessel_status(current_game):
    return current_game.check_sunk_vessel_status()


@then(parsers.parse("I know that the vessel {vessel_type} has been sunk"))
def then_i_know_that_the_vessel_has_been_sunk(sunk_vessel_status):
    assert sunk_vessel_status is True


@given("I have an empty target grid", target_fixture="target_grid")
def given_an_empty_target_grid(game):
    return game.current_player.target_grid


@when("game checks sunk vessel indicator", target_fixture="sunk_vessel_indicator")
def when_the_game_checks_sunk_vessel_indicator(game):
    return game.current_player.check_sunk_vessel_indicator()


@then("it contains 5 empty holes")
def then_it_contains_5_empty_holes(sunk_vessel_indicator):
    assert (sunk_vessel_indicator == np.zeros((5))).all()


@when("the game updates sunk vessel indicator", target_fixture="sunk_vessel_indicator")
def when_the_game_updates_sunk_vessel_indicator(current_game):
    current_game.update_sunk_vessel_indicator()
    return current_game.current_player.check_sunk_vessel_indicator()


@then("the red peg has been added to the sunk vessel indicator")
def then_the_game_adds_a_red_peg_to_sunk_vessel_indicator(sunk_vessel_indicator):
    assert (sunk_vessel_indicator == np.array([Peg.RED, 0, 0, 0, 0])).all()


@given("I have sunk 4 of the opponent's 5 vessels", target_fixture="current_game")
def given_i_have_sunk_4_of_the_opponents_5_vessels(game):
    num_of_vessels = 4
    vessels = [("D3", "BATTLESHIP"), ("A1", "CARRIER"), ("B4", "CRUISER"), ("J5", "SUBMARINE"), ("H8", "DESTROYER")]
    for (column, row), vessel in vessels[:num_of_vessels]:
        length = VesselLength[vessel]
        for i in range(length):
            game.current_player.target_grid.matrix[column_mapping[column]][i + row_mapping[row]] = Peg.RED
            game.opponent.ocean_grid.matrix[column_mapping[column]][i + row_mapping[row]] = VesselIdentifier[vessel]
    game.current_player.sunk_vessel_indicator = np.array(num_of_vessels * [Peg.RED] + [0])
    game.current_player.current_shot = (column_mapping["D"], row_mapping["3"])
    return game


@given("I have yet to hit one hole on the last vessel")
def given_i_have_yet_to_hit_one_hole_on_the_last_vessel(current_game):
    (column, row) = "H8"
    vessel = "DESTROYER"
    length = VesselLength[vessel]
    for i in range(length):
        current_game.opponent.ocean_grid.matrix[column_mapping[column]][i + row_mapping[row]] = VesselIdentifier[vessel]
    current_game.current_player.target_grid.matrix[column_mapping[column]][row_mapping[row]] = Peg.RED


@when("I take my turn to hit the last hole")
def when_I_take_my_turn_to_hit_the_last_hole(current_game):
    current_game.take_turn(("I", "8"))


@then("the game announces that I won")
def then_the_game_announces_that_I_won(current_game):
    assert current_game.status == GameStatus.PLAYER_1_WON
