from killer_queen.solver import Solver


def main():
    size = input("Enter the board size: ")
    s = Solver(int(size))
    solutions = s.solve()

    for index, solution in enumerate(solutions):
        print(f"\nSolution {index + 1}:")
        solution.display()


if __name__ == '__main__':
    main()
