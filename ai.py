from pieces_scores import *


class Player():

    def __init__(self):
        self.color = None

    def evaluate(self, board):

        board = str(board)

        score = 0

        board = board.replace('\n', ' ').split(' ')

        if self.color:
            whites = 1
            blacks = -1
        else:
            whites = -1
            blacks = 1

        j = 0

        for i in range(len(board)):

            piece = board[i]

            if piece == 'r':
                score += (50 + rook_eval_white[j]) * whites
            if piece == 'n':
                score += (30 + knight_eval_white[j]) * whites
            if piece == 'b':
                score += (30 + bishop_eval_white[j]) * whites
            if piece == 'q':
                score += (90 + queen_eval_white[j]) * whites
            if piece == 'k':
                score += (900 + king_eval_white[j]) * whites
            if piece == 'p':
                score += (10 + pawn_eval_white[j]) * whites

            if piece == 'R':
                score += (50 + rook_eval_black[j]) * blacks
            if piece == 'N':
                score += (30 + knight_eval_black[j]) * blacks
            if piece == 'B':
                score += (30 + bishop_eval_black[j]) * blacks
            if piece == 'Q':
                score += (90 + queen_eval_black[j]) * blacks
            if piece == 'K':
                score += (900 + king_eval_black[j]) * blacks
            if piece == 'P':
                score += (10 + pawn_eval_black[j]) * blacks

            j += 1

        return score

    def minimax(self, isMaxTurn, board, dimension, max_dimensions):

        dimension += 1

        scores = []
        for move in board.legal_moves:

            board.push(move)

            if dimension < max_dimensions:
                scores.append(self.minimax(
                    not isMaxTurn, board, dimension, max_dimensions))
            else:
                scores.append(self.evaluate(board))

            board.pop()

        return max(scores) if isMaxTurn else min(scores)

    def do_action(self, board):

        best_score = -1300

        if self.color == None:
            self.color = board.turn

        for move in board.legal_moves:

            board.push(move)

            score = self.minimax(False, board, 0, 2)
            if (score > best_score):
                best_score = score
                best_move = move

            board.pop()

        board.push(best_move)
