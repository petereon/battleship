Feature: Game Intialization
    Scenario: Game Unit Creation
        Given a new game
        When the game initialises
        Then the two game units are set up with grids
        And each grid is empty
        And each grid is 10 x 10
