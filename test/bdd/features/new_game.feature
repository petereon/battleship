Feature: Setting up a new game

    Scenario: Initial setup
        Given a new game
        And the interface is a console
        When the game is formatted
        Then the 10 x 10 board representing ocean grid of player 1 is in the 1 cell of the 2 row of a rich Table
        And the 10 x 10 board representing ocean grid of player 2 is in the 2 cell of the 2 row of a rich Table
        And the 10 x 10 board representing target grid of player 1 is in the 1 cell of the 1 row of a rich Table
        And the 10 x 10 board representing target grid of player 2 is in the 2 cell of the 1 row of a rich Table
