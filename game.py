import pygame
import chess
pygame.init()

color_primary = (167, 125, 92)
color_secondary = (232, 208, 168)
color_moving = (100, 111, 64)
color_possible_moves_playing = (130, 151, 105)

tile_size = 60

PIECE_NAMES = ['P', 'R', 'N', 'B', 'Q', 'K']
SQUARE_ROWS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']


class ChessGame():

    def __init__(self):

        self.screen = pygame.display.set_mode((tile_size * 8, tile_size * 8))
        pygame.display.set_caption('Chess MinMax')

        self.table = []
        color = True

        for y in range(8):

            self.table.append([])

            for x in range(8):

                self.table[-1].append(pygame.Surface((tile_size, tile_size)))
                if color:
                    self.table[-1][-1].fill(color_primary)

                else:
                    self.table[-1][-1].fill(color_secondary)

                color = not color

            color = not color

        self.board = chess.Board()

        self.pieces_texture = {}

        for piece in PIECE_NAMES:
            img = pygame.image.load(("img/w" + piece + ".png"))
            self.pieces_texture[piece] = pygame.transform.scale(
                img, (tile_size, tile_size))

            img = pygame.image.load(("img/b" + piece + ".png"))
            self.pieces_texture[piece.lower()] = pygame.transform.scale(
                img, (tile_size, tile_size))

        self.is_moving_piece = False

    def processClick(self, click):

        click = list(click)
        click = {
            'x': click[0] // tile_size,
            'y': click[1] // tile_size,
        }

        if self.is_moving_piece:
            old_click = self.piece_moving_position

            old_position = SQUARE_ROWS[old_click['x']
                                       ] + str(abs(old_click['y'] - 8))
            new_position = SQUARE_ROWS[click['x']] + str(abs(click['y'] - 8))

            if old_position != new_position:
                move = old_position + new_position
                move = chess.Move.from_uci(move)
                legal_moves = self.board.legal_moves
                if move in legal_moves:
                    self.board.push(move)

            self.table[self.piece_moving_position['x']][self.piece_moving_position['y']].fill(
                self.piece_moving_tile_color)
            self.is_moving_piece = False

        else:
            board_list = str(self.board).replace('\n', ' ').split(' ')
            if board_list[click['y'] * 8 + click['x']] != '.':
                self.piece_moving_position = click
                self.piece_moving_tile_color = self.table[click['x']][click['y']].get_at(
                    (0, 0))
                self.table[click['x']][click['y']].fill(color_moving)
                self.is_moving_piece = True

    def renderBoard(self):
        for y in range(8):
            for x in range(8):
                self.screen.blit(self.table[x][y],
                                 (x * tile_size, y * tile_size))

    def renderPieces(self):
        board_list = str(self.board).replace('\n', ' ').split(' ')

        for y in range(8):
            for x in range(8):
                img = board_list[x + 8 * y]
                if img != '.':
                    img = self.pieces_texture[img]
                    self.screen.blit(img, (x * tile_size, y * tile_size))

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.processClick(pygame.mouse.get_pos())

        self.screen.fill((0, 0, 0))

        self.renderBoard()

        self.renderPieces()

        pygame.display.update()
