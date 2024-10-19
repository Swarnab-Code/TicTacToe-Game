import pygame
from constants import *

def draw_lines(screen):
	# Draw horizontal and vertical lines to create the tic-tac-toe grid
	for i in range(1, 3):
		pygame.draw.line(screen, LINE_COLOR, (i * SQUARE_SIZE, 0), (i * SQUARE_SIZE, HEIGHT), LINE_WIDTH) # Vertical lines
		pygame.draw.line(screen, LINE_COLOR, (0, i * SQUARE_SIZE), (WIDTH, i * SQUARE_SIZE), LINE_WIDTH) # Horizontal lines

def draw_figures(screen, board):
	# Draw the figures (X and O) on the board
	for row in range(BOARD_ROWS):
		for col in range(BOARD_COLS):
			if board.board[row][col] == 1:
				pygame.draw.circle(screen, CIRCLE_COLOR, 
								   (int(col * SQUARE_SIZE + SQUARE_SIZE // 2), 
									int(row * SQUARE_SIZE + SQUARE_SIZE // 2)), 
								   CIRCLE_RADIUS, CIRCLE_WIDTH)
			elif board.board[row][col] == 2:
				pygame.draw.line(screen, CROSS_COLOR, 
								 (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE), 
								 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), 
								 CROSS_WIDTH)
				pygame.draw.line(screen, CROSS_COLOR, 
								 (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), 
								 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), 
								 CROSS_WIDTH)
				
def draw_vertical_winning_line(screen, col, player):
	posX = col * SQUARE_SIZE + SQUARE_SIZE // 2
	color = CIRCLE_COLOR if player == 1 else CROSS_COLOR
	pygame.draw.line(screen, color, (posX, 15), (posX, HEIGHT - 15), LINE_WIDTH)

def draw_horizontal_winning_line(screen, row, player):
	posY = row * SQUARE_SIZE + SQUARE_SIZE // 2
	color = CIRCLE_COLOR if player == 1 else CROSS_COLOR
	pygame.draw.line(screen, color, (15, posY), (WIDTH - 15, posY), LINE_WIDTH)

def draw_desc_diagonal(screen, player):
	color = CIRCLE_COLOR if player == 1 else CROSS_COLOR
	pygame.draw.line(screen, color, (15, 15), (WIDTH - 15, HEIGHT - 15), LINE_WIDTH)

def draw_asc_diagonal(screen, player):
	color = CIRCLE_COLOR if player == 1 else CROSS_COLOR
	pygame.draw.line(screen, color, (15, HEIGHT - 15), (WIDTH - 15, 15), LINE_WIDTH)
	