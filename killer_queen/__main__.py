from killer_queen.solver import Solver
from killer_queen.db import Session
from killer_queen.base_model import BaseModel


def main():
    BaseModel.metadata.create_all()

    size = input("Enter the board size: ")
    s = Solver(int(size))
    solutions = s.solve()

    session = Session()
    session.add_all(solutions)
    session.commit()
    session.close()


if __name__ == '__main__':
    main()
