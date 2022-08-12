from unittest import mock

import numpy as np
import pytest

from battleship.logic import Game, Grid
from battleship.logic.constants import (
    Peg,
    VesselIdentifier,
    VesselLength,
    column_mapping,
    row_mapping,
)


def test_game_initialization():
    assert isinstance(Game(), Game)


def describe_game_creates_grids():
    with mock.patch("battleship.logic.game.Player", return_value="testing"):
        game = Game()

        def test_game_creates_player1():
            assert game.player1 == "testing"

        def test_game_creates_player2():
            assert game.player2 == "testing"


def describe_check_shot_status():
    with mock.patch("battleship.logic.game.Player", return_value="testing") as player:
        player.ocean_grid = Grid()
        player.ocean_grid.matrix[column_mapping["B"]][row_mapping["2"]] = 2
        game = Game()
        game.opponent = player

        def test_shot_is_a_hit():
            assert game.check_shot_status(("B", "2")) is True

        def test_shot_is_a_miss():
            assert game.check_shot_status(("B", "3")) is False


def describe_place_peg_current_players_target_grid():
    def place_red_peg():
        game = Game()
        game.check_shot_status = mock.MagicMock(return_value=True)
        game.place_peg(("C", "5"))
        assert game.current_player.target_grid.matrix[column_mapping["C"]][row_mapping["5"]] == Peg.RED

    def place_white_peg():
        game = Game()
        game.check_shot_status = mock.MagicMock(return_value=False)
        game.place_peg(("A", "1"))
        assert game.current_player.target_grid.matrix[column_mapping["A"]][row_mapping["1"]] == Peg.WHITE


def test_place_red_peg_opponents_ocean_grid():
    game = Game()
    game.check_shot_status = mock.MagicMock(return_value=True)
    game.place_peg(("C", "5"))
    assert game.opponent.ocean_grid.matrix[column_mapping["C"]][row_mapping["5"]] == Peg.RED


def describe_check_sunk_vessel_status():
    def test_carrier_is_sunk():
        game = Game()
        length = VesselLength["CARRIER"]
        for i in range(length):
            game.current_player.target_grid.matrix[column_mapping["A"]][i] = Peg.RED
            game.opponent.ocean_grid.matrix[column_mapping["A"]][i] = VesselIdentifier["CARRIER"]
        game.current_player.current_shot = (column_mapping["A"], row_mapping["2"])
        assert game.check_sunk_vessel_status() is True

    def test_battleship_is_not_sunk():
        game = Game()
        length = VesselLength["BATTLESHIP"]
        game.current_player.target_grid.matrix[column_mapping["D"]][row_mapping["3"]] = Peg.RED
        for i in range(length):
            game.opponent.ocean_grid.matrix[column_mapping["D"]][i + 2] = VesselIdentifier["BATTLESHIP"]
        game.current_player.current_shot = (column_mapping["D"], row_mapping["3"])
        assert game.check_sunk_vessel_status() is False

    def test_battleship_is_sunk(get_game_with_D3_battleship):
        game = get_game_with_D3_battleship
        game.current_player.current_shot = (column_mapping["D"], row_mapping["3"])
        assert game.check_sunk_vessel_status() is True


@pytest.fixture
def get_game_with_D3_battleship():
    game = Game()
    length = VesselLength["BATTLESHIP"]
    for i in range(length):
        game.current_player.target_grid.matrix[column_mapping["D"]][i + 2] = Peg.RED
        game.opponent.ocean_grid.matrix[column_mapping["D"]][i + 2] = VesselIdentifier["BATTLESHIP"]
    return game


@pytest.fixture
def get_game_with_D3_battleship_and_A1_cruiser():
    game = Game()
    vessels = [("A1", "CARRIER"), ("D3", "BATTLESHIP")]
    for (column, row), vessel in vessels:
        length = VesselLength[vessel]
        for i in range(length):
            game.current_player.target_grid.matrix[column_mapping[column]][i + row_mapping[row]] = Peg.RED
            game.opponent.ocean_grid.matrix[column_mapping[column]][i + row_mapping[row]] = VesselIdentifier[vessel]
    game.sunk_vessel_indicator = np.array([Peg.RED, 0, 0, 0, 0])
    return game


def set_up_game_with_vessels(num_of_vessels):
    game = Game()
    vessels = [("D3", "BATTLESHIP"), ("A1", "CARRIER"), ("B4", "CRUISER"), ("J5", "SUBMARINE"), ("H8", "DESTROYER")]
    for (column, row), vessel in vessels[:num_of_vessels]:
        length = VesselLength[vessel]
        for i in range(length):
            game.current_player.target_grid.matrix[column_mapping[column]][i + row_mapping[row]] = Peg.RED
            game.opponent.ocean_grid.matrix[column_mapping[column]][i + row_mapping[row]] = VesselIdentifier[vessel]
    game.current_player.sunk_vessel_indicator = np.array(((num_of_vessels - 1) * [Peg.RED]) + ((6 - num_of_vessels) * [0]))
    return game


def describe_sunk_vessel_indicator():
    @pytest.mark.parametrize("num_vessels", [1, 2, 3, 4, 5])
    def test_game_updates_sunk_vessel_indicator_when_the_vessel_is_sunk(num_vessels):
        game = set_up_game_with_vessels(num_vessels)
        game.current_player.current_shot = (column_mapping["D"], row_mapping["3"])
        game.update_sunk_vessel_indicator()
        assert (game.current_player.sunk_vessel_indicator == np.array((num_vessels * [Peg.RED]) + ((5 - num_vessels) * [0]))).all()


def describe_game_take_turn():
    def test_take_turn_game_does_not_end_current_player_switches_to_player_2(get_game_with_D3_battleship_and_A1_cruiser):
        game = get_game_with_D3_battleship_and_A1_cruiser
        game.current_player.take_shot = mock.MagicMock()
        game.take_turn(("A", "1"))

        assert game.current_player == game.player2

    def test_take_turn_game_does_not_end_current_player_switches_to_player_1(get_game_with_D3_battleship_and_A1_cruiser):
        game = get_game_with_D3_battleship_and_A1_cruiser
        game.current_player = game.player2
        game.current_player.take_shot = mock.MagicMock()
        game.opponent = game.player1
        game.take_turn(("A", "1"))

        assert game.current_player == game.player1

    def test_take_turn_game_does_not_end_opponent_player_switches_to_player_1(get_game_with_D3_battleship_and_A1_cruiser):
        game = get_game_with_D3_battleship_and_A1_cruiser
        game.current_player.take_shot = mock.MagicMock()
        game.take_turn(("A", "1"))

        assert game.opponent == game.player1

    def test_take_turn_game_does_not_end_opponent_player_switches_to_player_2(get_game_with_D3_battleship_and_A1_cruiser):
        game = get_game_with_D3_battleship_and_A1_cruiser
        game.current_player = game.player2
        game.current_player.take_shot = mock.MagicMock()
        game.opponent = game.player1
        game.take_turn(("A", "1"))

        assert game.opponent == game.player2

    def test_take_turn_shot_is_made(get_game_with_D3_battleship_and_A1_cruiser):
        game = get_game_with_D3_battleship_and_A1_cruiser
        game.player2.take_shot = mock.MagicMock()
        game.current_player = game.player2
        game.opponent = game.player1
        game.take_turn(("A", "1"))

        game.player2.take_shot.assert_called_with(("A", "1"))


def describe_game_status_after_move():
    def test_game_does_not_end(get_game_with_D3_battleship_and_A1_cruiser):
        game = get_game_with_D3_battleship_and_A1_cruiser
        game.current_player.take_shot = mock.MagicMock()
        game.take_turn(("A", "1"))

        assert game.status is None
