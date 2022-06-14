import pickle
from unittest import mock
from unittest.mock import MagicMock

import numpy as np
import pytest
from pytest_bdd import given, parsers, scenarios, then, when
from rich.table import Table

import battleship
import battleship.cli.util as util

# Given a new game
# And two players
# And the interface is a console
# When the game starts
# Then the 10 x 10 board representing 1st player's ships is printed to the console on bottom-left
# And the 10 x 10 board representing 2nd player's ships are printed to the console on bottom-right
# And the 10 x 10 board representing 1st player's shots are printed to the console on top-left
# And the 10 x 10 board representing 2nd player's shots are printed to the console on top-right


scenarios("../features/new_game.feature")


def create_grid(title):
    grid = Table(title=title)
    grid.add_column("", justify="right", style="cyan", no_wrap=True)
    grid.add_column("A", justify="right", style="cyan", no_wrap=True)
    grid.add_column("B", justify="right", style="cyan", no_wrap=True)
    grid.add_column("C", justify="right", style="cyan", no_wrap=True)
    grid.add_column("D", justify="right", style="cyan", no_wrap=True)
    grid.add_column("E", justify="right", style="cyan", no_wrap=True)
    grid.add_column("F", justify="right", style="cyan", no_wrap=True)
    grid.add_column("G", justify="right", style="cyan", no_wrap=True)
    grid.add_column("H", justify="right", style="cyan", no_wrap=True)
    grid.add_column("I", justify="right", style="cyan", no_wrap=True)
    grid.add_column("J", justify="right", style="cyan", no_wrap=True)
    for count, data in enumerate(np.zeros((10, 10), dtype=int), start=1):
        grid.add_row(str(count), *list(map(str, data)))

    return grid


@pytest.fixture
def game_state():
    return {
        "player_1": {
            "ocean_grid": create_grid("Player 1's Ocean"),
            "target_grid": create_grid("Player 1's Target"),
        },
        "player_2": {
            "ocean_grid": create_grid("Player 2's Ocean"),
            "target_grid": create_grid("Player 2's Target"),
        },
    }


def new_add_row(*args):
    return args


@given("a new game", target_fixture="game")
def given_new_game():
    return battleship.initialise_game()


@given("the interface is a console", target_fixture="format")
def given_console_as_interface():
    return util.get_formatter("console")


@when("the game is formatted", target_fixture="table")
def when_game_is_printed(game, format):
    return format(game)
    # with mock.patch.object(Table, 'add_row', new=MagicMock()):
    #     return util.format_game(formatted_state)

    # pseudocode:
    # def print_game(game):
    #     table = Table(title="Battleship Game")
    #     table.add_column("Player 1")
    #     table.add_column("Player 2")
    #     table.add_row(game["player1"]["target_grid"], game["player2"]["target_grid])
    #     table.add_row(game["player1"]["ocean_grid"], game["player2"]["ocean_grid])
    # setattr(game, "__str__", print_game)
    # assert True == False


@then(
    parsers.parse(
        "the 10 x 10 board representing {grid} of {player} is in the {cell} cell of the {row} row of a rich Table",
    ),
)
def then_cell_contains(table, grid, player, cell, row, game_state):
    player = player.replace(" ", "_")
    grid = grid.replace(" ", "_")

    assert pickle.dumps(table.rows[row][cell]) == pickle.dumps(game_state[player][grid])

    # print(add_row_calls.call_args_list)
    # assert add_row_calls.call_args_list[1] == mock.call('Yay')
    # assert False
    # pseudocode: goes here
    # assert add_row_calls.cols == A-J
    # assert add_row_calls.rows == 1-10


# @then(
#     "the 10 x 10 board representing 2nd player's ships are printed to the console on bottom-right",
# )
# def then_board_bottom_right(add_row_calls, game):
#     pass
#     # assert add_row_calls.call_args_list[0] == mock.call('Blah')


# @then("the 10 x 10 board representing 1st player's shots are printed to the console on top-left")
# def then_board_top_left(add_row_calls, game, player_1_target_grid):

#     assert add_row_calls.call_args_list[0][0] == mock.call(player_1_target_grid())


# @then("the 10 x 10 board representing 2nd player's shots are printed to the console on top-right")
# def then_board_top_right(add_row_calls, game):
#     pass
