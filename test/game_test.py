from battleship.logic import Game, Grid


def test_game_initialization():
    assert isinstance(Game(), Game)


def describe_game_creates_grids():
    game = Game()

    def test_game_creates_player1_target_grid():
        assert isinstance(game.player1.unit.target_grid, Grid)
