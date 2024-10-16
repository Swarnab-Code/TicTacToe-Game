import pygame
from constants import *

def draw_lines(screen):
    # Draw horizontal and vertical lines to create the tic-tac-toe grid
    for i in range(1, 3):
        pygame.draw.line(screen, LINE_COLOR, (i * SQUARE_SIZE, 0), (i * SQUARE_SIZE, HEIGHT), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (0, i * SQUARE_SIZE), (WIDTH, i * SQUARE_SIZE), LINE_WIDTH)