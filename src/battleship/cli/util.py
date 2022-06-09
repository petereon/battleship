from typing import Any, Callable, List

import numpy as np
from rich.console import Console
from rich.table import Table


def get_formatter(interface: str) -> Callable[[dict], Any]:
    return format_for_console


def format_for_console(game: dict) -> dict:
    return {
        "player1": {
            "ocean_grid": format_table(game["player1"]["ocean_grid"], "Player 1's Ocean"),
            "target_grid": format_table(game["player1"]["target_grid"], "Player 1's Target"),
        },
        "player2": {
            "ocean_grid": format_table(game["player2"]["ocean_grid"], "Player 2's Ocean"),
            "target_grid": format_table(game["player2"]["target_grid"], "Player 2's Target"),
        },
    }


def format_table(board: np.ndarray, board_title: str) -> Table:
    table = Table(title=board_title)
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

    for count, data in enumerate(board, start=1):
        table.add_row(str(count), *list(map(str, data)))

    console = Console()
    console.print(table)

    return table
