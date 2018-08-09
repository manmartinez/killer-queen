from killer_queen.board import Board


class TestBoard:
    def test_placing_a_piece(self):
        b = Board(4)
        b.place(0, 1)
        assert b.positions[0][1] is True

    def test_removing_a_piece(self):
        b = Board(4)
        b.place(0, 1)
        b.remove(0, 1)
        assert b.positions[0][1] is False

    def test_has_piece(self):
        b = Board(4)
        b.place(0, 2)
        assert b.has_piece(0, 2)

    def test_board_does_not_have_piece(self):
        b = Board(4)
        assert b.has_piece(0, 1) is False

    def test_getting_piece_positions(self):
        b = Board(4)
        b.place(0, 2)
        b.place(1, 1)
        piece_positions = b.get_piece_positions()
        assert piece_positions == [(0, 2), (1, 1)]
