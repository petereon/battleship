import pytest
from pytest_bdd import given, parsers, scenarios, then, when

from battleship.logic import Grid, Player

scenarios("../features/shots.feature")


@pytest.fixture
def player():
    return Player()


@given("my target grid", target_fixture="target_grid")
def given_my_target_grid():
    # player = Player()
    # return player.target_grid
    return Grid()


@when(parsers.parse("I choose the hole {hole} on my target grid"), target_fixture="is_available")
def when_I_choose_the_hole_on_my_target_grid(hole, target_grid, player):
    player.target_grid = target_grid
    return player.is_hole_available(hole)


@then(parsers.parse("I know if it's available {available:b}"))
def then_I_know_if_it_s_available(available, is_available):
    assert is_available == available
