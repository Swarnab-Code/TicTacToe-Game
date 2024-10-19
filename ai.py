import copy
from board import Board

class AI:
	def __init__(self, player=2):
		self.player = player
		self.board = Board()

	# minimax
	def minimax(self, board, maximizing):
		# terminal case
		if board.check_win(1)[0]:
			return 1, None # opponent wins

		if board.check_win(self.player)[0]:
			return -1, None # ai wins

		if board.is_board_full():
			return 0, None # draw

		if maximizing:
			max_eval = -100
			best_move = None

			for row, col in board.get_available_squares():
				temp_board = copy.deepcopy(board)
				temp_board.mark_square(row, col, 1)
				score = self.minimax(temp_board, False)[0]
				if score > max_eval:
					max_eval = score
					best_move = (row, col)

			return max_eval, best_move

		else:
			min_eval = 100
			best_move = None

			for row, col in board.get_available_squares():
				temp_board = copy.deepcopy(board)
				temp_board.mark_square(row, col, self.player)
				score = self.minimax(temp_board, True)[0]
				if score < min_eval:
					min_eval = score
					best_move = (row, col)

			return min_eval, best_move
		
	# main evaluation
	def eval(self, board):
		# AI tries to maximize its score
		eval, move = self.minimax(board, False)

		print(f'AI has chosen to mark the square in pos {move} with an evaluation of: {eval}')

		return move # row, col
	
	def reset_ai(self):
		self.player = 2