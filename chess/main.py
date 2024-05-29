import pygame

pygame.init()

width, height = 800, 700
screen = pygame.display.set_mode((width, height))
font = pygame.font.Font('freesansbold.ttf', 20)
big_font = pygame.font.Font('freesansbold.ttf', 50)
timer = pygame.time.Clock()
fps = 60
pygame.display.set_caption("My Chess")

white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
white_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                   (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                   (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
captured_pieces_white = []
captured_pieces_black = [] 
turn = 0
selection = 100
valid_moves = []

#chess pieces img
black_queen = pygame.image.load('images/black queen.png')
black_queen = pygame.transform.scale(black_queen, (64, 64))
black_queen_small = pygame.transform.scale(black_queen, (36, 36))

black_king = pygame.image.load('images/black king.png')
black_king = pygame.transform.scale(black_king, (64, 64))
black_king_small = pygame.transform.scale(black_king, (36, 36))

black_rook = pygame.image.load('images/black rook.png')
black_rook = pygame.transform.scale(black_rook, (64, 64))
black_rook_small = pygame.transform.scale(black_rook, (36, 36))

black_bishop = pygame.image.load('images/black bishop.png')
black_bishop = pygame.transform.scale(black_bishop, (64, 64))
black_bishop_small = pygame.transform.scale(black_bishop, (36, 36))

black_knight = pygame.image.load('images/black knight.png')
black_knight = pygame.transform.scale(black_knight, (64, 64))
black_knight_small = pygame.transform.scale(black_knight, (36, 36))

black_pawn = pygame.image.load('images/black pawn.png')
black_pawn = pygame.transform.scale(black_pawn, (52, 52))
black_pawn_small = pygame.transform.scale(black_pawn, (36, 36))


white_queen = pygame.image.load('images/white queen.png')
white_queen = pygame.transform.scale(white_queen, (64, 64))
white_queen_small = pygame.transform.scale(white_queen, (36, 36))

white_king = pygame.image.load('images/white king.png')
white_king = pygame.transform.scale(white_king, (64, 64))
white_king_small = pygame.transform.scale(white_king, (36, 36))

white_rook = pygame.image.load('images/white rook.png')
white_rook = pygame.transform.scale(white_rook, (64, 64))
white_rook_small = pygame.transform.scale(white_rook, (36, 36))

white_bishop = pygame.image.load('images/white bishop.png')
white_bishop = pygame.transform.scale(white_bishop, (64, 64))
white_bishop_small = pygame.transform.scale(white_bishop, (36, 36))

white_knight = pygame.image.load('images/white knight.png')
white_knight = pygame.transform.scale(white_knight, (64, 64))
white_knight_small = pygame.transform.scale(white_knight, (36, 36))

white_pawn = pygame.image.load('images/white pawn.png')
white_pawn = pygame.transform.scale(white_pawn, (52, 52))
white_pawn_small = pygame.transform.scale(white_pawn, (36, 36))

white_images = [white_pawn, white_queen, white_king, white_knight, white_rook, white_bishop]
small_white_images = [white_pawn_small, white_queen_small, white_king_small, white_knight_small, white_rook_small, white_bishop_small]

black_images = [black_pawn, black_queen, black_king, black_knight, black_rook, black_bishop]
small_black_images = [black_pawn_small, black_queen_small, black_king_small, black_knight_small, black_rook_small, black_bishop_small]

piece_list = ['pawn', 'queen', 'king', 'knight', 'rook', 'bishop']

#game board
def draw_board():
    for i in range(32):
        column = i % 4
        row = i // 4
        if row % 2 == 0:
            pygame.draw.rect(screen, 'light gray', [480 - (column * 160), row * 80, 80, 80])
        else:
            pygame.draw.rect(screen, 'light gray', [560 - (column * 160), row * 80, 80, 80])
        pygame.draw.rect(screen, 'gray', [0, 640, width, 160])
        pygame.draw.rect(screen, 'gold', [0, 640, width, 160], 5)
        pygame.draw.rect(screen, 'gold', [640, 0, 160, height], 5)

        status_text = ['White: Select a piece', 'White: Move a piece','Black: Select a piece', 'Black: Move a piece']
        screen.blit(big_font.render(status_text[turn], True, 'black'), (15, 650))
        for i in range(9):
            pygame.draw.line(screen, 'black', (0, 80 * i), (640, 80 * i), 3) 
            pygame.draw.line(screen, 'black', (80 * i, 0), (80*i, 640), 3) 

def draw_pieces():
    for i in range(len(white_pieces)):
        index = piece_list.index(white_pieces[i])
        if white_pieces[i] == 'pawn':
            screen.blit(white_pawn, (white_locations[i][0] * 80 + 17, white_locations[i][1] * 80 + 24))
        else:
            screen.blit(white_images[index], (white_locations[i][0] * 80 + 8, white_locations[i][1] * 80 + 8))
        if turn < 2:
            if selection == i:
                pygame.draw.rect(screen, 'red', [white_locations[i][0] * 80 + 1, white_locations[i][1] * 80 + 1, 80, 80], 2)

    for i in range(len(black_pieces)):
        index = piece_list.index(black_pieces[i])
        if black_pieces[i] == 'pawn':
            screen.blit(black_pawn, (black_locations[i][0] * 80 + 17, black_locations[i][1] * 80 + 24))
        else:
            screen.blit(black_images[index], (black_locations[i][0] * 80 + 8, black_locations[i][1] * 80 + 8))
        if turn >= 2:
            if selection == i:
                pygame.draw.rect(screen, 'blue', [black_locations[i][0] * 80 + 1, black_locations[i][1] * 80 + 1, 80, 80], 2)

def check_options(pieces, locations, turn):
    moves_list = []
    all_move_list = []
    for i in range((len(pieces))):
        location = locations[i]
        piece = pieces[i]
        if piece == 'pawn':
            moves_list = check_pawn(location, turn)
        # elif piece == 'rook':
        #     moves_list = black_rook(location, turn)
        # elif piece == 'knight':
        #     moves_list = check_knight(location, turn)
        # elif piece == 'bishop':
        #     moves_list = check_bishop(location, turn)
        # elif piece == 'queen':
        #     moves_list = check_queen(location, turn)
        # elif piece == 'king':
        #     moves_list = check_king(location, turn)
        # all_move_list.append(moves_list)
    return all_move_list

def check_pawn(position, color):
    moves_list = []
    if color == 'white':
        if (position[0], position[1] + 1) not in white_locations and \
        (position[0], position[1] + 1) not in black_locations and position[1] > 7:
            moves_list.append((position[0], position[1] + 1))

        if (position[0], position[1] + 2) not in white_locations and \
        (position[0], position[1] + 2) not in black_locations and position[1] == 1:
            moves_list.append((position[0], position[1] + 2))

        if (position[0] + 1, position[1] + 1 in black_locations):
            moves_list.append((position[0] + 1, position[1] + 1))
        if (position[0] - 1, position[1] + 1) in black_locations:
            moves_list.append((position[0] - 1, position[1] + 1))

    else :
        if (position[0], position[1] - 1) not in white_locations and \
        (position[0], position[1] - 1) not in black_locations and position[1] < 0:
            moves_list.append((position[0], position[1] + 1))

        if (position[0], position[1] - 2) not in white_locations and \
        (position[0], position[1] - 2) not in black_locations and position[1] == 6:
            moves_list.append((position[0], position[1] + 2))

        if (position[0] + 1, position[1] - 1 in white_locations):
            moves_list.append((position[0] + 1, position[1] - 1))
        if (position[0] - 1, position[1] - 1) in white_locations:
            moves_list.append((position[0] - 1, position[1] - 1))

    return moves_list

def check_valid_moves():
    if turn < 2:
        options_list = white_options
    else:
        options_list = black_options
    valid_options = options_list[selection]
    return valid_options

def draw_valid(moves):
    if turn < 2:
        color = 'red'
    else:
        color = 'blue'
    for i in range(len(moves)):
        pygame.draw.circle(screen, color, (moves[i][0] * 80 + 40, moves[i][1] * 80 + 40), 5)


# Main game loop
black_options = check_options(black_pieces, black_locations, 'black')
white_options = check_options(white_pieces, white_locations, 'white')
running = True
while running:
    timer.tick(fps)
    screen.fill('white')

    draw_board()
    draw_pieces()
    if selection != 100:
        valid_moves = check_valid_moves()
        draw_valid(valid_moves)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x_coord = event.pos[0] // 80
            y_coord = event.pos[1] // 80
            click_coord = (x_coord, y_coord)
            if turn <= 1:
                if click_coord in white_locations:
                    selection = white_locations.index(click_coord)
                    if turn == 0:
                        turn = 1
                if click_coord in valid_moves and selection != 100:
                    white_locations[selection] = click_coord
                    if click_coord in black_locations:
                        black_piece = black_locations.index(click_coord)
                        captured_pieces_white.append(black_pieces[black_piece])
                        black_pieces.pop(black_piece)
                        black_locations.pop(black_piece)
                    black_options = check_options(black_pieces, black_locations, 'black')
                    white_options = check_options(white_pieces, white_locations, 'white')
                    turn = 2
                    selection = 100
                    valid_moves = []

            if turn > 1:
                if click_coord in black_locations:
                    selection = black_locations.index(click_coord)
                    if turn == 2:
                        turn = 3
                if click_coord in valid_moves and selection != 100:
                    black_locations[selection] = click_coord
                    if click_coord in white_locations:
                        white_piece = white_locations.index(click_coord)
                        captured_pieces_black.append(white_pieces[white_piece])
                        white_pieces.pop(white_piece)
                        white_locations.pop(white_piece)
                    black_options = check_options(black_pieces, black_locations, 'black')
                    white_options = check_options(white_pieces, white_locations, 'white')
                    turn = 0
                    selection = 100
                    valid_moves = []

    pygame.display.flip()
pygame.quit()