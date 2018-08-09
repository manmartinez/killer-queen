from app.board import Board

class TestBoard:
  def test_placing_a_piece(self):
    b = Board(4)
    b.place(0, 1)
    assert b.positions[0][1] == True

  def test_removing_a_piece(self):
    b = Board(4)
    b.place(0, 1)

    b.remove(0, 1)

    assert b.positions[0][1] == False

  def test_has_piece(self):
    b = Board(4)
    b.place(0, 2)

    assert b.has_piece(0, 2)

  def test_board_does_not_have_piece(self):
    b = Board(4)

    assert b.has_piece(0, 1) == False