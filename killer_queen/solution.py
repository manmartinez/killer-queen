from killer_queen.board import Board


class Solution:

    def __init__(self, size, positions):
        self.size = size
        self.positions = positions
        self._board = None

    def display(self):
        board = self._get_board()
        board.display()

    def _get_board(self):
        if self._board is None:
            self._board = self._build_board()
        return self._board

    def _build_board(self):
        board = Board(self.size)
        for position in self.positions:
            board.place(*position)
        return board
