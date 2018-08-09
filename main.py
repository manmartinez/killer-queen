from app.solver import Solver

size = input("Enter the board size: ")
s = Solver(int(size))
solutions = s.solve()

for index, solution in enumerate(solutions):
  print("\nSolution %s:" % (index + 1))
  solution.display()
