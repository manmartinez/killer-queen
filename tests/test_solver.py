import pytest

from killer_queen.solver import Solver


class TestSolver:

    @pytest.mark.parametrize("board_size,expected_solutions", [
        (6, 4), (7, 40), (8, 92)])
    def test_solution_size(self, board_size, expected_solutions):
        solver = Solver(board_size)
        solutions = solver.solve()
        assert len(solutions) == expected_solutions
