from typing import List

import pytest
from rich.table import Table

import minesweeper.cli.util as util

rows = [i for i in range(10)]


@pytest.fixture
def game_state():
    return {
        "player1": {
            "own_board": [
                [rows],
                [rows],
                [rows],
                [rows],
                [rows],
                [rows],
                [rows],
                [rows],
                [rows],
                [rows],
            ],
            "shots_board": [
                [rows],
                [rows],
                [rows],
                [rows],
                [rows],
                [rows],
                [rows],
                [rows],
                [rows],
                [rows],
            ],
        },
        "player2": {
            "own_board": [
                [rows],
                [rows],
                [rows],
                [rows],
                [rows],
                [rows],
                [rows],
                [rows],
                [rows],
                [rows],
            ],
            "shots_board": [
                [rows],
                [rows],
                [rows],
                [rows],
                [rows],
                [rows],
                [rows],
                [rows],
                [rows],
                [rows],
            ],
        },
    }


def describe_get_formatter():
    def test_get_console_player1_own_board_contents(game_state):
        formatter = util.get_formatter("console")
        tables: List[Table] = formatter(game_state)
        table_player1_own_board = tables[0]

        expected_table = Table(title="Player 1's Ocean")
        for i in range(10):
            expected_table.add_row(str(i + 1), *list(map(str, rows)))
        assert table_player1_own_board.rows == expected_table.rows

    def test_get_console_player1_own_board_headers(game_state):
        formatter = util.get_formatter("console")
        tables: List[Table] = formatter(game_state)
        table_player1_own_board = tables[0]

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
