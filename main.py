from game import ChessGame
from ai import Player

game = ChessGame()
player = Player()

while True:
    game.update()
    if not game.board.turn:
        player.do_action(game)
