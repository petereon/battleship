Feature: Ship Placement

    Scenario Outline: Placing a carrier
        Given a player
        And the player's grids are set up
        When the player places the carrier on their ocean grid
        And chooses the position <position>
        Then a carrier is placed on the ocean grid
        And the carrier is in position <position>
        And the carrier has 5 holes

        Examples:
            | position |
            | -------- |
            | A1, A5   |
            | A1, E1   |
            | J5, J9   |
