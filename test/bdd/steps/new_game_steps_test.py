import pytest
from pytest_bdd import given, scenarios, then, when

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


@given("a new game", target_fixture="game")
def given_new_game():
    return battleship.initialise_game()


@given("the interface is a console", target_fixture="format")
def given_console_as_interface():
    return util.get_formatter("console")


@when("the game is printed", target_fixture="representation")
def when_game_is_printed(game, format):
    # pseudocode:
    # def print_game(game):
    #     table = Table(title="Battleship Game")
    #     table.add_column("Player 1")
    #     table.add_column("Player 2")
    #     table.add_row(game["player1"]["target_grid"], game["player2"]["target_grid])
    #     table.add_row(game["player1"]["ocean_grid"], game["player2"]["ocean_grid])
    # setattr(game, "__str__", print_game)
    return print(format(game))


@then("the 10 x 10 board representing 1st player's ships is printed to the console on bottom-left")
def then_board_bottom_left(representation):
    # pseudocode: goes here
    # assert representation.cols == A-J
    # assert representation.rows == 1-10
    pass


@then(
    "the 10 x 10 board representing 2nd player's ships are printed to the console on bottom-right",
)
def then_board_bottom_right(representation):
    pass


@then("the 10 x 10 board representing 1st player's shots are printed to the console on top-left")
def then_board_top_left(representation):
    pass


@then("the 10 x 10 board representing 2nd player's shots are printed to the console on top-right")
def then_board_top_right(representation):
    pass
