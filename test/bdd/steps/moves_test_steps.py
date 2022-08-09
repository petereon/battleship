import json

import pytest
from pytest_bdd import given, parsers, scenarios, then, when

from battleship.logic import Game, Grid, Player
from battleship.logic.constants import Peg, column_mapping, row_mapping

scenarios("../features/moves.feature")


@pytest.fixture
def game():
    return Game()


@pytest.fixture
def player():
    return Player()


@given("my target grid", target_fixture="target_grid")
def given_my_target_grid():
    return Grid()


@given(parsers.parse("a hole {hole} is already taken"))
def given_the_hole_is_already_taken(hole, target_grid):
    column, row = (column_mapping[hole[0]], row_mapping[hole[1]])
    target_grid.matrix[column][row] = Peg.RED


@when(parsers.parse("I choose the hole {hole} on my target grid"), target_fixture="is_available")
def when_I_choose_the_hole_on_my_target_grid(hole, target_grid, player):
    player.target_grid = target_grid

    return player.is_hole_available(hole)


@then(parsers.parse("I know if it's available {available}"), converters={"available": json.loads})
def then_I_know_if_it_s_available(available, is_available):
    assert is_available == available


@given(parsers.parse("I have taken a shot at the hole {hole}"), target_fixture="target_hole")
def given_i_have_taken_a_shot_at_the_hole(hole):
    return hole


@given(parsers.parse("the opponent's ocean grid with hole {hole} is filled {is_filled}"), converters={"is_filled": json.loads})
def given_the_opponents_ocean_grid(game, hole, is_filled):
    column, row = (column_mapping[hole[0]], row_mapping[hole[1]])
    game.opponent.ocean_grid.matrix[column][row] = is_filled


@when("the game checks the shot status", target_fixture="shot_status")
def when_the_game_checks_the_shot_status(target_hole, game):
    return game.check_shot_status(target_hole)


@then(parsers.parse("the status is {status}"), converters={"status": json.loads})
def given_a_player(status, shot_status):
    assert shot_status == status


@given(parsers.parse("it was a {smth}"))
def given_it_was_a_hit_or_miss():
    pass


@given(parsers.parse("opponent's ocean grid has a vessel at hole {hole}"))
def given_target_grid_has_a_vessel_at_hole(hole, game):
    column, row = (column_mapping[hole[0]], row_mapping[hole[1]])
    grid = Grid()
    game.opponent.ocean_grid = grid
    grid.matrix[column][row] = 9


@when(parsers.parse("the game places the peg on my target grid at {hole}"))
def when_the_game_places_the_peg_on_my_target_grid(hole, game):
    game.place_peg(hole)


@then(parsers.parse("the color of the target grid peg is {color}"))
def then_the_color_of_the_target_grid_peg_is_red(target_hole, game, color):
    column, row = (column_mapping[target_hole[0]], row_mapping[target_hole[1]])
    assert game.current_player.target_grid.matrix[column][row] == Peg.RED if color == "red" else Peg.WHITE


@then("the color of the ocean grid peg is red")
def then_the_color_of_the_ocean_grid_peg_is_red(target_hole, game):
    column, row = (column_mapping[target_hole[0]], row_mapping[target_hole[1]])
    assert game.opponent.ocean_grid.matrix[column][row] == Peg.RED


@when(parsers.parse("the game places the peg on opponent's ocean grid at {hole}"))
def when_the_game_places_the_peg_on_opponents_ocean_grid(hole, game):
    game.place_peg(hole)
