from unittest import mock

from battleship.logic import Game, Player


def test_game_initialization():
    assert isinstance(Game(), Game)


def describe_game_creates_grids():
    with mock.patch("battleship.logic.game.Player", return_value="testing"):
        game = Game()

        def test_game_creates_player1():
            assert game.player1 == "testing"

        def test_game_creates_player2():
            assert game.player2 == "testing"
