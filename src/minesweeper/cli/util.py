from typing import Any, Callable, List

from rich.table import Table


def get_formatter(interface: str) -> Callable[[dict], Any]:
    return format_for_console


# {
#         "player1": {
#             "own_board": [[rows], [rows], [rows], [rows], [rows], [rows], [rows], [rows], [rows], [rows]],
#             "shots_board": [[rows], [rows], [rows], [rows], [rows], [rows], [rows], [rows], [rows], [rows]],
#         },
#         "player2": {
#             "own_board": [[rows], [rows], [rows], [rows], [rows], [rows], [rows], [rows], [rows], [rows]],
#             "shots_board": [[rows], [rows], [rows], [rows], [rows], [rows], [rows], [rows], [rows], [rows]],
#         },
#     }


def format_for_console(game: dict) -> List[Table]:

    table_player1_own_board = Table(title="Player 1's Ocean")
    table_player1_own_board.add_column("", justify="right", style="cyan", no_wrap=True)
    table_player1_own_board.add_column("A", justify="right", style="cyan", no_wrap=True)
    table_player1_own_board.add_column("B", justify="right", style="cyan", no_wrap=True)
    table_player1_own_board.add_column("C", justify="right", style="cyan", no_wrap=True)
    table_player1_own_board.add_column("D", justify="right", style="cyan", no_wrap=True)
    table_player1_own_board.add_column("E", justify="right", style="cyan", no_wrap=True)
    table_player1_own_board.add_column("F", justify="right", style="cyan", no_wrap=True)
    table_player1_own_board.add_column("G", justify="right", style="cyan", no_wrap=True)
    table_player1_own_board.add_column("H", justify="right", style="cyan", no_wrap=True)
    table_player1_own_board.add_column("I", justify="right", style="cyan", no_wrap=True)
    table_player1_own_board.add_column("J", justify="right", style="cyan", no_wrap=True)

    for count, data in enumerate(game["player1"]["own_board"], start=1):
        table_player1_own_board.add_row(str(count), *list(map(str, data[0])))

    return [table_player1_own_board]
