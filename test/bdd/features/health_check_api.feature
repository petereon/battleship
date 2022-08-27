Feature: Battleship health check

    Scenario: The application can be monitored using the health endpoint
        Given a battleships HTTP API
        And the API is running
        When I send an HTTP GET request to the `health` endpoint
        Then health endpoint responds with code 200
