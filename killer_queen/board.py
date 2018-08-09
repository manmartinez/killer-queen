class Board:

    def __init__(self, size):
        self.size = size
        self._init_positions()

    def has_piece(self, row, col):
        return self.positions[row][col]

    def place(self, row, col):
        self.positions[row][col] = True

    def remove(self, row, col):
        self.positions[row][col] = False

    def get_piece_positions(self):
        piece_positions = []

        for row in range(self.size):
            for col in range(self.size):
                if self.has_piece(row, col):
                    piece_positions.append((row, col))

        return piece_positions

    def display(self):
        for row in self.positions:
            print('|', end='')
            for value in row:
                char = 'Q|' if value else '_|'
                print(char, end='')
            print('')

    def _init_positions(self):
        self.positions = [
            [False for i in range(self.size)]
            for i in range(self.size)
        ]
