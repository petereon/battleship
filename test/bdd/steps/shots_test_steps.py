import json

import pytest
from pytest_bdd import given, parsers, scenarios, then, when

from battleship.logic import Grid, Player
from battleship.logic.constants import Peg, column_mapping, row_mapping

scenarios("../features/shots.feature")


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
    print(f"is_available: {is_available}", f"available: {available}")
    assert is_available == available
