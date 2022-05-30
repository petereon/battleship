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


# def test_example():
#     from rich.console import Console

#     table = Table(title="Star Wars Movies")

#     table.add_column("Released", justify="right", style="cyan", no_wrap=True)
#     table.add_column("Title", style="magenta")
#     table.add_column("Box Office", justify="right", style="green")

#     table.add_row("Dec 20, 2019", "Star Wars: The Rise of Skywalker", "$952,110,690")
#     table.add_row("May 25, 2018", "Solo: A Star Wars Story", "$393,151,347")
#     table.add_row("Dec 15, 2017", "Star Wars Ep. V111: The Last Jedi", "$1,332,539,889")
#     table.add_row("Dec 16, 2016", "Rogue One: A Star Wars Story", "$1,332,439,889")

#     console = Console()
#     console.print(table)
#     console.print(table.rows[1])
#     assert False


def describe_get_formatter():
    def test_get_console_player1_own_board_contents(game_state):
        formatter = util.get_formatter("console")
        tables: List[Table] = formatter(game_state)
        table_player1_own_board = tables[0]

        assert table_player1_own_board.rows == [
            [[1] + rows],
            [[2] + rows],
            [[3] + rows],
            [[4] + rows],
            [[5] + rows],
            [[6] + rows],
            [[7] + rows],
            [[8] + rows],
            [[9] + rows],
            [[10] + rows],
        ]

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
