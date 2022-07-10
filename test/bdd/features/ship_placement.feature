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
            | A 1, A 5   |
            | A 1, E 1   |
            | J 5, J 9   |

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
            | A 1, A 4   |
            | B 1, E 1   |
            | J 5, J 8   |

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
            | H 1, H 3   |
            | C 1, E 1   |
            | J 5, J 7   |

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
            | H 7, H 9   |
            | C 2, E 2   |
            | J 5, J 7   |

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
            | H 7, H 8   |
            | D 2, E 2   |
            | J 5, J 6   |

    Scenario Outline: Placing a destroyer in an invalid position
        Given a player
        And the player's grids are set up
        When the player places the destroyer on their ocean grid
        And chooses an invalid position <position>
        Then the player receives an error message
        And there is no change to their ocean grid

        Examples:
            | position   |
            | H H, H 8   |
            | A 4, C 5   |
            | A 7, A 10  |
            | D 2, bl ah |
            | J 10, J 12 |
