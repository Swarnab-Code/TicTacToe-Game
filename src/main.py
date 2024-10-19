import pygame
import sys
from constants import *
from draw import draw_lines
from game import Game

# Initialize pygame
pygame.init()

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
icon = pygame.image.load('assets/icon/logo.png')
pygame.display.set_icon(icon)
pygame.display.set_caption("TIC TAC TOE")
screen.fill(BG_COLOR)

# Initialize the game
game = Game(screen)
draw_lines(screen)

# Main loop
while True:
	# Handle events
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.MOUSEBUTTONDOWN and not game.board.game_over:
			mouseX = event.pos[0] # x
			mouseY = event.pos[1] # y

			clicked_row = int(mouseY // SQUARE_SIZE)
			clicked_col = int(mouseX // SQUARE_SIZE)

			game.play(clicked_row, clicked_col)

		if event.type == pygame.KEYDOWN:
			
			if event.key == pygame.K_g:
				game.change_gamemode()

			if event.key == pygame.K_r:
				game.restart()

	# ai initial call
	if game.gamemode == 'ai' and game.board.player == game.ai.player and not game.board.game_over:
		pygame.display.update()
		row, col = game.ai.eval(game.board)
		game.play(row, col)

	game.show_winner() # Show the winner or draw message
	pygame.display.update()
