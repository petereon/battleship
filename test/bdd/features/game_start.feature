Feature: Game Intialization
    Scenario: Game Unit Creation
        Given a new game
        When the game initialises
        Then the player 1 is set up with the ocean grid
        And the player 1 is set up with the target grid
        And the player 2 is set up with the ocean grid
        And the player 2 is set up with the target grid
        And the ocean grid for player 1 is empty
        And the target grid for player 1 is empty
        And the ocean grid for player 2 is empty
        And the target grid for player 2 is empty
        And the ocean grid for player 1 is 10 x 10
        And the target grid for player 1 is 10 x 10
        And the ocean grid for player 2 is 10 x 10
        And the target grid for player 2 is 10 x 10
