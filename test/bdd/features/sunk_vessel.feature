Feature: Sunk vessel

    Scenario Outline: Checking the sunk vessel status
        Given I have sunk a vessel <vessel_type>
        When the game checks the sunk vessel status
        Then I know that the vessel <vessel_type> has been sunk

        Examples:
            | vessel_type |
            | carrier     |
            | battleship  |
            | cruiser     |
            | submarine   |
