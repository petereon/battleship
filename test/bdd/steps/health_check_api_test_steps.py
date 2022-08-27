import numpy as np
from fastapi.testclient import TestClient
from pytest_bdd import given, scenarios, then, when

from battleship.api import app

scenarios("../features/health_check_api.feature")
HTTP_OK = 200


@given("a battleships HTTP API", target_fixture="api")
def given_a_battleships_http_api():
    return app


@given("the API is running", target_fixture="http_api")
def given_the_api_is_running(api):
    return TestClient(api)


@when("I send an HTTP GET request to the `health` endpoint", target_fixture="health_response")
def when_i_send_an_http_get_request_to_the_health_endpoint(http_api):
    return http_api.get("/health")


@then("health endpoint responds with code 200")
def then_the_health_endpoint_responds_with_ok_code(health_response):
    assert health_response.status_code == HTTP_OK
