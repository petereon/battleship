from pytest_bdd import given, parsers, scenarios, then, when

scenarios("../features/ship_placement.feature")

# Feature: Ship Placement

#     Scenario Outline: Placing a carrier
#         Given a player
#         And the player's grids are set up
#         When the player places the carrier on their ocean grid
#         And chooses the position <position>
#         Then a carrier is placed on the ocean grid
#         And the carrier is in position <position>
#         And the carrier has 5 holes

#         Examples:
#             | position |
#             | -------- |
#             | A1, A5   |
#             | A1, E1   |
#             | J5, J9   |


@given("a player")
def given_a_player():
    pass


@given("the player's grids are set up")
def given_players_grids_are_set_up():
    pass


@when("the player places the carrier on their ocean grid")
def when_the_player_places_the_carrier():
    pass


@when(parsers.parse("chooses the position {position}"))
def when_the_player_chooses_the_position(position):
    pass


@then("a carrier is placed on the ocean grid")
def then_a_carrier_is_placed_on_the_ocean_grid():
    pass


@then(parsers.parse("the carrier is in position {position}"))
def then_the_carrier_is_in_position(position):
    pass


@then("the carrier has 5 holes")
def then_the_carrier_has_5_holes():
    pass
