Feature: Ship Placement

    Scenario Outline: Placing a carrier
        Given a player
        And the player's grids are set up
        When the player places the carrier on their ocean grid
        And chooses the position <position>
        Then the carrier in position <position> on the ocean grid
        And the carrier has 5 holes
        And they are in a straight line

        Examples:
            | position |
            | -------- |
            | A1, A5   |
            | A1, E1   |
            | J5, J9   |
