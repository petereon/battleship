import pickle
from typing import List
from unittest.mock import patch

import numpy as np
import pytest
from rich.console import Console
from rich.table import Table

import battleship.cli.util as util

rows = [i for i in range(10)]

console = Console()


@pytest.fixture
def game_state():
    return {
        "player1": {
            "ocean_grid": np.zeros((10, 10), dtype=int),
            "target_grid": np.zeros((10, 10), dtype=int),
        },
        "player2": {
            "ocean_grid": np.zeros((10, 10), dtype=int),
            "target_grid": np.zeros((10, 10), dtype=int),
        },
    }


def mock_format_table(title):
    table = Table(title=title)
    table.add_column("", justify="right", style="cyan", no_wrap=True)
    table.add_column("A", justify="right", style="cyan", no_wrap=True)
    table.add_column("B", justify="right", style="cyan", no_wrap=True)
    table.add_column("C", justify="right", style="cyan", no_wrap=True)
    table.add_column("D", justify="right", style="cyan", no_wrap=True)
    table.add_column("E", justify="right", style="cyan", no_wrap=True)
    table.add_column("F", justify="right", style="cyan", no_wrap=True)
    table.add_column("G", justify="right", style="cyan", no_wrap=True)
    table.add_column("H", justify="right", style="cyan", no_wrap=True)
    table.add_column("I", justify="right", style="cyan", no_wrap=True)
    table.add_column("J", justify="right", style="cyan", no_wrap=True)

    for count, data in enumerate(np.zeros((10, 10), dtype=int), start=1):
        table.add_row(str(count), *list(map(str, data)))

    return table


PLAYER_1 = 0
PLAYER_2 = 1
TARGET_GRID = 0
OCEAN_GRID = 1


def describe_get_formatter():
    @patch("battleship.cli.util.format_table", lambda *args: mock_format_table("Player 1's Ocean"))
    def test_get_console_player1_ocean_grid(game_state):
        formatter = util.get_formatter("console")
        table: Table = formatter(game_state)
        table_player1_ocean_grid = table.columns[PLAYER_1]._cells[OCEAN_GRID]

        expected_table = mock_format_table("Player 1's Ocean")
        assert pickle.dumps(table_player1_ocean_grid) == pickle.dumps(
            expected_table,
        ), console.print(table_player1_ocean_grid)

    @patch("battleship.cli.util.format_table", lambda *args: mock_format_table("Player 1's Target"))
    def test_get_console_player1_target_grid_contents(game_state):
        formatter = util.get_formatter("console")
        table: Table = formatter(game_state)
        table_player1_target_grid = table.columns[PLAYER_1]._cells[TARGET_GRID]

        expected_table = mock_format_table("Player 1's Target")
        assert pickle.dumps(table_player1_target_grid) == pickle.dumps(
            expected_table,
        ), console.print(table_player1_target_grid)

    @patch("battleship.cli.util.format_table", lambda *args: mock_format_table("Player 2's Ocean"))
    def test_get_console_player2_ocean_grid_contents(game_state):
        formatter = util.get_formatter("console")
        table: Table = formatter(game_state)
        table_player2_ocean_grid = table.columns[PLAYER_2]._cells[OCEAN_GRID]

        expected_table = mock_format_table("Player 2's Ocean")
        assert pickle.dumps(table_player2_ocean_grid) == pickle.dumps(
            expected_table,
        ), console.print(table_player2_ocean_grid)

    @patch("battleship.cli.util.format_table", lambda *args: mock_format_table("Player 2's Target"))
    def test_get_console_player2_target_grid_contents(game_state):
        formatter = util.get_formatter("console")
        table: Table = formatter(game_state)
        table_player2_target_grid = table.columns[PLAYER_2]._cells[TARGET_GRID]

        expected_table = mock_format_table("Player 2's Target")
        assert pickle.dumps(table_player2_target_grid) == pickle.dumps(
            expected_table,
        ), console.print(table_player2_target_grid)


def test_format_for_console(game_state, mocker):
    with patch("battleship.cli.util.format_table", lambda x, _: x):
        assert util.format_for_console(game_state) == game_state


def describe_format_table():
    def test_table_title():
        board = np.zeros((10, 10), dtype=int)
        table: Table = util.format_table(board, "Test Player's Board")

        assert table.title == "Test Player's Board"

    def test_table_x_axis():
        board = np.zeros((10, 10), dtype=int)
        table: Table = util.format_table(board, "Test Player's Board")

        assert [i.header for i in table.columns] == [
            "",
            "A",
            "B",
            "C",
            "D",
            "E",
            "F",
            "G",
            "H",
            "I",
            "J",
        ]

    def test_table_y_axis():
        board = np.zeros((10, 10), dtype=int)
        table: Table = util.format_table(board, "Test Player's Board")
        assert [i for i in table.columns[0]._cells] == [
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
        ]

    def test_table_values():
        board = np.zeros((10, 10), dtype=int)
        table: Table = util.format_table(board, "Test Player's Board")
        for col in table.columns[1:]:
            assert [i for i in col._cells] == [
                "0",
                "0",
                "0",
                "0",
                "0",
                "0",
                "0",
                "0",
                "0",
                "0",
            ]


# def describe_game_print(mock_state_with_tables):
#     def test_player1_target_grid():
#             game_repr = util.format_game(mock_state_with_tables)
#             game_repr.rows[0][0] = mock_state_with_tables["player1"]["target_grid"]
