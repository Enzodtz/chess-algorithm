import pygame
pygame.init()

table_color_primary = (167, 125, 92)
table_color_secondary = (232, 208, 168)
table_color_moving = (0, 255, 0)

tile_size = 60

class ChessGame():

    def __init__(self):

        self.screen = pygame.display.set_mode((tile_size * 8, tile_size * 8))
        pygame.display.set_caption('Chess game')

        self.table = []
        color = True

        for y in range(8):

            self.table.append([])

            for x in range(8):

                self.table[-1].append(pygame.Surface((tile_size, tile_size)))
                if color:
                    self.table[-1][-1].fill(table_color_primary)

                else:
                    self.table[-1][-1].fill(table_color_secondary)

                color = not color

            color = not color

        self.pieces =  [['bR', 'bN', 'bB', 'bK', 'bQ', 'bB', 'bN', 'bR'],
                        ['bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp'],
                        ['--', '--', '--', '--', '--', '--', '--', '--'],
                        ['--', '--', '--', '--', '--', '--', '--', '--'],
                        ['--', '--', '--', '--', '--', '--', '--', '--'],
                        ['--', '--', '--', '--', '--', '--', '--', '--'],
                        ['wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp'],
                        ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR']]

        all_pieces = ['bR', 'bN', 'bB', 'bK', 'bQ', 'bp', 'wR', 'wN', 'wB', 'wK', 'wQ', 'wp']
        self.pieces_texture = {}
        for piece in all_pieces:

            img = pygame.image.load(("img/" + piece + ".png"))
            self.pieces_texture[piece] = pygame.transform.scale(img, (tile_size, tile_size))

        self.is_moving_piece = False

    def validMove(self, click, piece_clicked):

        if self.piece_moving[0] == piece_clicked[0]:
            return False

        if self.piece_moving == '--':
            return False

        if self.piece_moving[1] == 'p':
            return self.pawnMove(click, piece_clicked)
        
        return False

    def pawnMove(self, click, piece_clicked):

        piece = self.piece_moving_position 

        if self.piece_moving[0] == 'w':
            if piece[1] <= click[1]:
                return False

            if piece[1] - 2 > click[1]:
                return False

        if self.piece_moving[0] == 'b':
            if piece[1] >= click[1]:
                return False

            if piece[1] + 2 < click[1]:
                return False

        if piece_clicked == '--': 
            if piece[0] != click[0]:
                return False

        else:
            if piece[0] != click[0] + 1 and piece[0] != click[0] - 1:
                return False

            if self.piece_moving[0] == 'w':
                if piece[1] != click[1] + 1:
                    return False

            if self.piece_moving[0] == 'b':
                if piece[1] != click[1] - 1: 
                    return False

        return True

    def processClick(self, click):

        click = list(click)
        click[0] = (click[0] // tile_size)
        click[1] = (click[1] // tile_size)

        piece_clicked = self.pieces[click[1]][click[0]]

        if self.is_moving_piece:

            if self.validMove(click, piece_clicked):
         
                self.pieces[self.piece_moving_position[1]][self.piece_moving_position[0]] = '--'
                self.pieces[click[1]][click[0]] = self.piece_moving
                
            self.table[self.piece_moving_position[0]][self.piece_moving_position[1]].fill(self.piece_moving_tile_color)
            self.is_moving_piece = False

        else:
            
            if piece_clicked != '--': 

                self.piece_moving = self.pieces[click[1]][click[0]]
                self.piece_moving_position = click

                self.piece_moving_tile_color = self.table[click[0]][click[1]].get_at((0,0))
                self.table[click[0]][click[1]].fill(table_color_moving)

                self.is_moving_piece = True

    def renderBoard(self):

        for y in range(8):
            for x in range(8):

                self.screen.blit(self.table[x][y], (x * tile_size, y * tile_size))

    def renderPieces(self):

        for y in range(8):
            for x in range(8):
                
                piece = self.pieces[y][x]

                if piece != '--':
                    self.screen.blit(self.pieces_texture[piece], (tile_size * x, tile_size * y))

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

game = ChessGame()
game.update()

import time
while True:
    game.update()
    time.sleep(0.02)