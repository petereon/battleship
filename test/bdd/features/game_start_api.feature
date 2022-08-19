Feature: Game Initialization from the API
    Scenario: Sending an HTTP GET request to the `new_game` endpoint
        Given a battleships HTTP API
        When I send an HTTP GET request to the `new_game` endpoint
        Then a new game gets created with an ID
