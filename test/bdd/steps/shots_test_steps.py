import json

import pytest
from pytest_bdd import given, parsers, scenarios, then, when

from battleship.logic import Game, Grid, Player
from battleship.logic.constants import Peg, column_mapping, row_mapping

scenarios("../features/shots.feature")


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
    return (column_mapping[hole[0]], row_mapping[hole[1]])


@given("the opponent's ocean grid")
def given_the_opponents_ocean_grid():
    game = Game()
    return game.opponent.ocean_grid


@when("the game checks the shot status", target_fixture="shot_status")
def when_the_game_checks_the_shot_status(target_hole):
    return game.check_shot_status(target_hole)


@then(parsers.parse("the status is {status}"))
def given_a_player(status, shot_status):
    assert shot_status == status
