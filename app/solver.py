from app.board import Board
from app.solution import Solution

class Solver:
  def __init__(self, size):
    self.board = Board(size)

  def solve(self):
    self._solutions = []
    self._place_in_row(0)
    return self._solutions

  def _place_in_row(self, row):
    if row == self.board.size:
      self._add_solution()
    else:
      self._try_in_row(row)

  def _add_solution(self):
    piece_positions = self.board.get_piece_positions()
    solution = Solution(self.board.size, piece_positions)
    self._solutions.append(solution)

  def _try_in_row(self, row):
    for col in range(self.board.size):
      if self._is_valid(row, col):
        self.board.place(row, col)
        self._place_in_row(row + 1)
        self.board.remove(row, col)

  def _is_valid(self, row, col):
    return self._top_is_clear(row, col) and \
           self._top_left_is_clear(row, col) and \
           self._top_right_is_clear(row, col)

  def _top_is_clear(self, row, col):
    row -= 1

    while row >= 0:
      if self.board.has_piece(row, col):
        return False
      row -= 1

    return True

  def _top_left_is_clear(self, row, col):
    row -= 1
    col -= 1

    while row >= 0 and col >= 0:
      if self.board.has_piece(row, col):
        return False
      row -= 1
      col -= 1

    return True

  def _top_right_is_clear(self, row, col):
    row -= 1
    col += 1

    while row >= 0 and col < self.board.size:
      if self.board.has_piece(row, col):
        return False
      col += 1
      row -= 1

    return True
