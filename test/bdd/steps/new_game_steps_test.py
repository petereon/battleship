import pytest
from pytest_bdd import given, scenario, then, when

import minesweeper
import minesweeper.cli.util as util

# Given a new game
# And two players
# And the interface is a console
# When the game starts
# Then the 10 x 10 board representing 1st player's ships is printed to the console on bottom-left
# And the 10 x 10 board representing 2nd player's ships are printed to the console on bottom-right
# And the 10 x 10 board representing 1st player's shots are printed to the console on top-left
# And the 10 x 10 board representing 2nd player's shots are printed to the console on top-right


@scenario("new_game.feature", "Initial setup")
def test_setting_up_a_new_game():
    pass


@given("a new game", target_fixture="game")
def new_game():
    return minesweeper.initialise_game()


@given("the interface is a console", target_fixture="format")
def console_as_interface():
    return util.get_formatter("console")


@when("the game is printed", target_fixture="representation")
def game_is_printed(game, format):
    print(game)
    return format(game)


@then("the 10 x 10 board representing 1st player's ships is printed to the console on bottom-left")
def board_bottom_left(representation):
    pass


@then(
    "the 10 x 10 board representing 2nd player's ships are printed to the console on bottom-right",
)
def board_bottom_right(representation):
    pass


@then("the 10 x 10 board representing 1st player's shots are printed to the console on top-left")
def board_top_left(representation):
    pass


@then("the 10 x 10 board representing 2nd player's shots are printed to the console on top-right")
def board_top_right(representation):
    pass
