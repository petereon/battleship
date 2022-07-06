Feature: Ship Placement

    Scenario Outline: Placing a carrier in position
        Given a player
        And the player's grids are set up
        When the player places the carrier on their ocean grid
        And chooses the position <position>
        Then the carrier in position <position> on the ocean grid
        And the carrier has 5 holes
        And they are in a straight line

        Examples:
            | position |
            | A1, A5   |
            | A1, E1   |
            | J5, J9   |

    Scenario Outline: Placing a battleship in position
        Given a player
        And the player's grids are set up
        When the player places the battleship on their ocean grid
        And chooses the position <position>
        Then the battleship in position <position> on the ocean grid
        And the battleship has 4 holes
        And they are in a straight line

        Examples:
            | position |
            | A1, A4   |
            | B1, E1   |
            | J5, J8   |

    Scenario Outline: Placing a cruiser in position
        Given a player
        And the player's grids are set up
        When the player places the cruiser on their ocean grid
        And chooses the position <position>
        Then the cruiser in position <position> on the ocean grid
        And the cruiser has 3 holes
        And they are in a straight line

        Examples:
            | position |
            | H1, H3   |
            | C1, E1   |
            | J5, J7   |

    Scenario Outline: Placing a submarine in position
        Given a player
        And the player's grids are set up
        When the player places the submarine on their ocean grid
        And chooses the position <position>
        Then the submarine in position <position> on the ocean grid
        And the submarine has 3 holes
        And they are in a straight line

        Examples:
            | position |
            | H7, H9   |
            | C2, E2   |
            | J5, J7   |

    Scenario Outline: Placing a destroyer in position
        Given a player
        And the player's grids are set up
        When the player places the destroyer on their ocean grid
        And chooses the position <position>
        Then the destroyer in position <position> on the ocean grid
        And the destroyer has 2 holes
        And they are in a straight line

        Examples:
            | position |
            | H7, H8   |
            | D2, E2   |
            | J5, J6   |
