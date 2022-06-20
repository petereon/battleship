import numpy as np
from pytest_bdd import given, scenarios, then, when

from battleship.logic import Game, Grid

scenarios("../features/game_start.feature")


@given("a new game")
def given_new_game():
    pass


@when("the game initialises", target_fixture="game")
def when_the_game_initialises():
    return Game()


@then("the two game units are set up with grids")
def then_game_units_are_set_up(game):
    assert isinstance(game.player1.unit.ocean_grid, Grid)
    assert isinstance(game.player1.unit.target_grid, Grid)
    assert isinstance(game.player2.unit.ocean_grid, Grid)
    assert isinstance(game.player2.unit.target_grid, Grid)


@then("each grid is empty")
def then_each_grid_is_empty(game):
    assert len(np.where(game.player1.unit.ocean_grid != 0)) == 0
    assert len(np.where(game.player1.unit.target_grid != 0)) == 0
    assert len(np.where(game.player2.unit.ocean_grid != 0)) == 0
    assert len(np.where(game.player2.unit.target_grid != 0)) == 0


@then("each grid is 10 x 10")
def then_each_grid_is_10_x_10(game):
    assert game.player1.unit.ocean_grid.shape == (10, 10)
    assert game.player1.unit.target_grid.shape == (10, 10)
    assert game.player2.unit.ocean_grid.shape == (10, 10)
    assert game.player2.unit.target_grid.shape == (10, 10)
