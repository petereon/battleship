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
