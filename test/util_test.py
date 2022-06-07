from typing import List
from unittest.mock import patch

import numpy as np
import pytest
from rich.table import Table

import minesweeper.cli.util as util

rows = [i for i in range(10)]


@pytest.fixture
def game_state():
    return {
        "player1": {
            "own_board": np.zeros((10, 10), dtype=int),
            "shots_board": np.zeros((10, 10), dtype=int),
        },
        "player2": {
            "own_board": np.zeros((10, 10), dtype=int),
            "shots_board": np.zeros((10, 10), dtype=int),
        },
    }


def mock_format_table():
    table = Table(title="board_title")
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


def describe_get_formatter():
    @patch("minesweeper.cli.util.format_table", lambda *args: mock_format_table())
    def test_get_console_player1_own_board_contents(game_state):
        formatter = util.get_formatter("console")
        tables: List[Table] = formatter(game_state)
        table_player1_own_board = tables["player1"]["own_board"]

        expected_table = Table(title="Player 1's Ocean")
        for i in range(10):
            expected_table.add_row(str(i + 1), *list(map(str, rows)))
        assert table_player1_own_board.rows == expected_table.rows

    @patch("minesweeper.cli.util.format_table", lambda *args: mock_format_table())
    def test_get_console_player1_own_board_headers(game_state):
        formatter = util.get_formatter("console")
        tables: List[Table] = formatter(game_state)
        table_player1_own_board = tables["player1"]["own_board"]

        assert [i.header for i in table_player1_own_board.columns] == [
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

    @patch("minesweeper.cli.util.format_table", lambda *args: mock_format_table())
    def test_get_console_player1_shots_board_contents(game_state):
        formatter = util.get_formatter("console")
        tables: List[Table] = formatter(game_state)
        table_player1_shots_board = tables["player1"]["shots_board"]

        expected_table = Table(title="Player 1's Shots")
        for i in range(10):
            expected_table.add_row(str(i + 1), *list(map(str, rows)))
        assert table_player1_shots_board.rows == expected_table.rows

    @patch("minesweeper.cli.util.format_table", lambda *args: mock_format_table())
    def test_get_console_player2_own_board_contents(game_state):
        formatter = util.get_formatter("console")
        tables: List[Table] = formatter(game_state)
        table_player1_own_board = tables["player2"]["own_board"]

        expected_table = Table(title="Player 2's Ocean")
        for i in range(10):
            expected_table.add_row(str(i + 1), *list(map(str, rows)))
        assert table_player1_own_board.rows == expected_table.rows

    @patch("minesweeper.cli.util.format_table", lambda *args: mock_format_table())
    def test_get_console_player2_shots_board_contents(game_state):
        formatter = util.get_formatter("console")
        tables: List[Table] = formatter(game_state)
        table_player1_shots_board = tables["player2"]["shots_board"]

        expected_table = Table(title="Player 2's Shots")
        for i in range(10):
            expected_table.add_row(str(i + 1), *list(map(str, rows)))
        assert table_player1_shots_board.rows == expected_table.rows


def test_format_for_console(game_state, mocker):
    with patch("minesweeper.cli.util.format_table", lambda x, _: x):
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
