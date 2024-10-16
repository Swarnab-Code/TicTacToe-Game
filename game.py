from board import Board

class Game:
    def __init__(self):
        self.board = Board()

    def play(self, row, col):
        if self.board.available_square(row, col):
            self.board.mark_square(row, col) # Mark the square for the current player

            self.board.player = self.board.player % 2 + 1
