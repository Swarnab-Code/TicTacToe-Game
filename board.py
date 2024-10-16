import numpy as np
from constants import *

class Board:
    def __init__(self):
        self.board = np.zeros((BOARD_ROWS, BOARD_COLS)) # Initialize the game board
        self.player = 1 # Start with player 1

    def mark_square(self, row, col):
        # Mark the square with the current player (1 for O, 2 for X)
        self.board[row, col] = self.player

    def available_square(self, row, col ):
        # Check if the square is available
        return self.board[row, col] == 0
    
    def is_board_full(self):
        # Check if the board is full
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if self.board[row][col] == 0:
                    return False
        return True
