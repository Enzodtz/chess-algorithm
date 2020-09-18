import chess
import random
import ai

game = chess.Board()

player = ai.Player()
player_2 = ai.Player()

while not game.is_variant_end():

    print(game, '\n')
    player.do_action(game)
    print(game, '\n')
    player_2.do_action(game)