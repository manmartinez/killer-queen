from sqlalchemy import Column, Integer, JSON
from killer_queen.board import Board
from killer_queen.base_model import BaseModel


class Solution(BaseModel):
    __tablename__ = 'solutions'

    id = Column(Integer, primary_key=True, autoincrement=True)
    size = Column(Integer, nullable=False)
    positions = Column(JSON, nullable=False)

    def display(self):
        board = self._get_board()
        board.display()

    def _get_board(self):
        if not hasattr(self, '_board'):
            self._board = self._build_board()
        return self._board

    def _build_board(self):
        board = Board(self.size)
        for position in self.positions:
            board.place(*position)
        return board
