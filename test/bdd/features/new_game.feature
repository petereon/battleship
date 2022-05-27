Feature: Setting up a new game

    Scenario: Initial setup
        Given a new game
        And the interface is a console
        When the game is printed
        Then the 10 x 10 board representing 1st player's ships is printed to the console on bottom-left
        And the 10 x 10 board representing 2nd player's ships are printed to the console on bottom-right
        And the 10 x 10 board representing 1st player's shots are printed to the console on top-left
        And the 10 x 10 board representing 2nd player's shots are printed to the console on top-right
