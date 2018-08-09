class Board:
  def __init__(self, size):
    self.size = size
    self._initPositions()

  def has_piece(self, row, col):
    return self.positions[row][col]

  def place(self, row, col):
    self.positions[row][col] = True

  def remove(self, row, col):
    self.positions[row][col] = False

  def display(self):
    for row in self.positions:
      print('|', end='')
      for value in row:
        char = 'Q|' if value else '_|'
        print(char, end='')
      print('')

  def _initPositions(self):
    self.positions = [
      [False for i in range(self.size)]
      for i in range(self.size)
    ]
