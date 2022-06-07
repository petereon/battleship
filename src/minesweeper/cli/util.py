from typing import Any, Callable, List

import numpy as np
from rich.console import Console
from rich.table import Table


def get_formatter(interface: str) -> Callable[[dict], Any]:
    return format_for_console


def format_for_console(game: dict) -> dict:
    return {
        "player1": {
            "own_board": format_table(game["player1"]["own_board"], "Player 1"),
            "shots_board": format_table(game["player1"]["shots_board"], "Player 1"),
        },
        "player2": {
            "own_board": format_table(game["player2"]["own_board"], "Player 2"),
            "shots_board": format_table(game["player2"]["shots_board"], "Player 2"),
        },
    }


def format_table(board: np.ndarray, player: str) -> Table:
    table = Table(title=f"{player}'s Ocean")
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
