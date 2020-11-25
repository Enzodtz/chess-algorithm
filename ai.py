from pieces_scores import *


class Player():

    def __init__(self):
        self.color = None
        self.whites = None

    def evaluate(self, board):

        score = 0
        board = str(board).replace('\n', ' ').split(' ')

        for i in range(len(board)):

            piece = board[i]

            if piece == 'r':
                score += rook_value * self.whites * -1
            if piece == 'n':
                score += knight_value * self.whites * -1
            if piece == 'b':
                score += bishop_value * self.whites * -1
            if piece == 'q':
                score += queen_value * self.whites * -1
            if piece == 'p':
                score += pawn_value * self.whites * -1

            if piece == 'R':
                score += rook_value * self.whites
            if piece == 'N':
                score += knight_value * self.whites
            if piece == 'B':
                score += bishop_value * self.whites
            if piece == 'Q':
                score += queen_value * self.whites
            if piece == 'P':
                score += pawn_value * self.whites

        return score

    def minimax(self, isMaxTurn, board, dimension):

        dimension -= 1

        scores = []
        for move in board.legal_moves:

            board.push(move)

            if dimension != 0:
                scores.append(self.minimax(
                    not isMaxTurn, board, dimension))
            else:
                evaluation = self.evaluate(board)
                scores.append(evaluation)

            board.pop()

        if scores == []:
            if board.is_game_over():
                result = board.result()

                if result == '1-0':
                    scores = [1000 * self.whites]
                elif result == '0-1':
                    scores = [-1000 * self.whites]
                else:
                    scores = [0]
            else:
                scores = [0]

        return max(scores) if isMaxTurn else min(scores)

    def do_action(self, board):

        best_score = -1000

        if self.color == None:
            self.color = board.turn
            self.whites = 1 if self.color else -1

        for move in board.legal_moves:

            board.push(move)

            score = self.minimax(False, board, 1)
            if (score > best_score):
                best_score = score
                best_move = move

            board.pop()

        board.push(best_move)
