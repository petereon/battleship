Feature: Shots taken during the game

    Scenario Outline: The game player makes a move by choosing a target hole on their target grid
        Given my target grid
        And a hole <taken_hole> is already taken
        When I choose the hole <hole> on my target grid
        Then I know if it's available <available>

        Examples:
            | hole | taken_hole | available |
            | A1   | B2         | true      |
            | H8   | H8         | false     |
            | B7   | A1         | true      |


    Scenario Outline: Status is announced after each shot
        Given I have taken a shot at the hole <hole>
        And the opponent's ocean grid with hole <hole> is filled <is_filled>
        When the game checks the shot status
        Then the status is <status>

        Examples:
            | hole | is_filled | status |
            | A1   | true      | true   |
            | A1   | false     | false  |
            | J5   | true      | true   |

    Scenario Outline: The game player makes a move by choosing a target hole on their target grid and hits
        Given I have taken a shot at the hole <hole>
        And it was a hit
        And opponent's ocean grid has a vessel at hole <hole>
        When the game places the peg on my target grid at <hole>
        Then the color of the target grid peg is red

        Examples:
            | hole |
            | B5   |
            | C9   |

    Scenario Outline: The opponent player updates their ocean grid with the move that current player made

        Given I have taken a shot at the hole <hole>
        And it was a hit
        And opponent's ocean grid has a vessel at hole <hole>
        When the game places the peg on opponent's ocean grid at <hole>
        Then the color of the ocean grid peg is red

        Examples:
            | hole |
            | C3   |
            | J5   |

    Scenario Outline: The game player makes a move by choosing a target hole on their target grid and misses
        Given I have taken a shot at the hole <hole>
        And it was a miss
        And opponent's ocean grid has a vessel at hole <hole>
        When the game places the peg on my target grid at <hole>
        Then the color of the target grid peg is white

        Examples:
            | hole |
            | B5   |
            | C9   |

    Scenario: After each move has been made.  The game passes the initiative to the opponent.
        Given current player's target grid
        And the current player is player 1
        And opponent's target grid
        When current player takes their turn
        Then the game does not end
        And the current player is player 2
        And player 2 can take the shot
