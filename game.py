from constants import *
from board import Board
from draw import draw_lines, draw_vertical_winning_line, draw_horizontal_winning_line, draw_desc_diagonal, draw_asc_diagonal

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.board = Board()

    def play(self, row, col):
        if self.board.available_square(row, col):
            # Mark the square for the current player
            self.board.mark_square(row, col)
            if self.check_winner():
                self.board.game_over = True
            # Switch player
            self.board.player = self.board.player % 2 + 1

    def check_winner(self):
        # Check if the current player has won
        win_type, index = self.board.check_win(self.board.player)
        if win_type:
            self.board.game_over = True
            if win_type == "vertical":
                draw_vertical_winning_line(self.screen, index, self.board.player)
            elif win_type == "horizontal":
                draw_horizontal_winning_line(self.screen, index, self.board.player)
            elif win_type == "desc_diagonal":
                draw_desc_diagonal(self.screen, self.board.player)
            elif win_type == "asc_diagonal":
                draw_asc_diagonal(self.screen, self.board.player)

    def restart(self):
        # Restart the game
        self.board.reset()
        self.screen.fill(BG_COLOR)
        draw_lines(self.screen)
        self.board.player = 1 # Reset to player 1
        self.board.game_over = False
