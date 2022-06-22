from numpy import ndarray

from battleship.logic import Grid


def test_grid_initialization():
    assert isinstance(Grid(), Grid)


def describe_matrix():
    grid = Grid()

    def test_grid_is_a_10_x_10_array():
        assert grid.matrix.shape == (10, 10)

    def test_grid_is_a_numpy_array():
        assert isinstance(grid.matrix, ndarray)
