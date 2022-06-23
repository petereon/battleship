import numpy as np
from pytest_bdd import given, parsers, scenarios, then, when

from battleship.logic import Game, Grid

scenarios("../features/game_start.feature")


@given("a new game")
def given_new_game():
    pass


@when("the game initialises", target_fixture="game")
def when_the_game_initialises():
    return Game()


@then(parsers.parse("the player {player} is set up with the {grid} grid"))
def then_the_player_is_set_up_with_grid(game, player, grid):
    assert isinstance(
        game.__getattribute__(f"player{player}").__getattribute__(f"{grid}_grid"),
        Grid,
    )


@then(parsers.parse("the {grid} grid for player {player} is empty"))
def then_the_grid_is_empty(game, grid, player):
    assert np.all(
        game.__getattribute__(f"player{player}").__getattribute__(f"{grid}_grid").matrix == 0,
    )


@then(parsers.parse("the {grid} grid for player {player} is 10 x 10"))
def then_the_grid_is_10x10(game, grid, player):
    assert np.all(
        game.__getattribute__(f"player{player}").__getattribute__(f"{grid}_grid").matrix.shape == (10, 10),
    )
