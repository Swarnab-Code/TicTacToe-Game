import pygame
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
            # Check if there is any winner for the current mark
            if self.check_winner():
                self.board.game_over = True
            elif self.board.is_board_full():
                # Check for a draw
                self.board.game_over = True
            else:
                # Switch player only if the game is not over
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
            return True # A player has won
        return False # No winner

    def show_winner(self):
        font = pygame.font.Font(None, 74)
        if self.board.game_over:
            if self.check_winner():
                winner_text = f"PLAYER {self.board.player} WINS!"
            else:
                winner_text = "DRAW!"
            
            text_surface = font.render(winner_text, True, (255, 255, 255), (0, 0, 0))
            text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))  # Center the text
            self.screen.blit(text_surface, text_rect)
            pygame.display.update()
            pygame.time.wait(3000) # Show the message for 3 sec
            self.restart()

    def restart(self):
        # Restart the game
        self.board.reset()
        self.screen.fill(BG_COLOR)
        draw_lines(self.screen)
        self.board.player = 1 # Reset to player 1
        self.board.game_over = False
