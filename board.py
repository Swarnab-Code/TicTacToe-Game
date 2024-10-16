import numpy as np
from constants import *

class Board:
    def __init__(self):
        self.board = np.zeros((BOARD_ROWS, BOARD_COLS)) # Initialize the game board
        self.player = 1 # Start with player 1
        self.game_over = False # Track if the game is over

    def mark_square(self, row, col):
        # Mark the square with the current player (1 for O, 2 for X)
        self.board[row, col] = self.player

    def available_square(self, row, col):
        # Check if the square is available
        return self.board[row, col] == 0
    
    def is_board_full(self):
        # Check if the board is full
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if self.board[row][col] == 0:
                    return False
        return True
    
    def check_win(self, player):
        return (self.check_columns(player) or
                self.check_rows(player) or
                self.check_diagonals(player)) or (None, None)

    def check_columns(self, player):
        for col in range(3):
            if np.all(self.board[:, col] == player):
                return "vertical", col
        return None
        
    def check_rows(self, player):
        for row in range(3):
            if np.all(self.board[row] == player):
                return "horizontal", row
        return None

    def check_diagonals(self, player):
        if np.all(np.diag(self.board) == player):
            return "desc_diagonal", None

        if np.all(np.diag(np.fliplr(self.board)) == player):
            return "asc_diagonal", None
        
        return None

    def reset(self):
        # Reset the board for a new game
        self.board = np.zeros((BOARD_ROWS, BOARD_COLS))  
        
