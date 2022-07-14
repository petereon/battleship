Feature: Shots taken during the game

    Scenario Outline: The game player makes a move by choosing a target hole on their target grid
        Given my target grid
        When I choose the hole <hole> on my target grid
        Then I know if it's available <available>

        Examples:
            | hole | available |
            | A1   | true      |
            | H8   | false     |
            | B7   | true      |
