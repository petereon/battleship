import numpy as np
from fastapi.testclient import TestClient
from pytest_bdd import given, parsers, scenarios, then, when

# from battleship.api import app

# scenarios("../features/game_start_api.feature")

# @given("a battleships HTTP API", target_fixture="http_api")
# def given_a_battleships_HTTP_API():
#     return TestClient(app)

# @when("I send an HTTP GET request to the `new_game` endpoint")
# def when_I_send_a_request_to_the_new_game_endpoint(http_api):
#     res = http_api.get('new_game')
