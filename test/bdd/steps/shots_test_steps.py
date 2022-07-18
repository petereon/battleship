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


@given("an ocean grid", target_fixture="ocean_grid")
def given_an_ocean_grid():
    return Grid()


@given(parsers.parse("an available hole {hole}"), target_fixture="target_hole")
def given_an_available_hole(hole):
    return hole


@given("a player")
def given_a_player(game, player):
    game.player = player


@when("I take my shot")
def when_take_shot(hole, player):
    column, row = (column_mapping[hole[0]], row_mapping[hole[1]])
    player.take_shot((column, row))


@when("I check the game status", target_fixture="game_status")
def when_I_check_the_game_status(game, capsys):
    game.check_game_status()
    return capsys.readouterr().out


@then(parsers.parse("the game announces if the shot was a {status}"))
def then_game_announces_status(game_status, status):
    assert game_status == status
