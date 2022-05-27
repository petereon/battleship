import pytest
from pytest_bdd import given, scenario, then, when

import minesweeper

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


@given("a new game")
def new_game():
    assert False


@given("the interface is a console")
def console_as_interface():
    pass


@when("the game is printed")
def game_is_printed():
    pass


@then("the 10 x 10 board representing 1st player's ships is printed to the console on bottom-left")
def board_bottom_left():
    pass


@then(
    "the 10 x 10 board representing 2nd player's ships are printed to the console on bottom-right",
)
def board_bottom_right():
    pass


@then("the 10 x 10 board representing 1st player's shots are printed to the console on top-left")
def board_top_left():
    pass


@then("the 10 x 10 board representing 2nd player's shots are printed to the console on top-right")
def board_top_right():
    pass
