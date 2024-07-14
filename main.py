import pygame
import sys

pygame.init()
pygame.font.init()

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1000

font = pygame.font.Font('Mitr-Bold.ttf', 74)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Jogo da Velha')

def draw_hash():
    pygame.draw.line(screen, (97, 84, 88), (859, 241), (859, 839), 9)
    pygame.draw.line(screen, (97, 84, 88), (1059, 241), (1059, 839), 9)
    pygame.draw.line(screen, (97, 84, 88), (660, 440), (1260, 440), 9)
    pygame.draw.line(screen, (97, 84, 88), (660, 641), (1260, 641), 9)

def draw_circle(coordinate):
    pygame.draw.circle(screen, (211, 173, 105), coordinate, 75, 15)

def draw_x(coordinate1, coordinate2, coordinate3, coordinate4):
    pygame.draw.line(screen, (58, 163, 148), coordinate1, coordinate2, 25)
    pygame.draw.line(screen, (58, 163, 148), coordinate3, coordinate4, 25)

def write(phrase, coordinate, color):
    text = font.render(phrase, True, color)
    text_rect = text.get_rect(center=coordinate)
    screen.blit(text, text_rect)

def get_clicked_cell(mouse_pos):
    x, y = mouse_pos
    row = (y - 241) // 200  # calcula a linha baseado na posição do clique
    col = (x - 660) // 200  # calcula a coluna baseado na posição do clique
    return (row, col)

def is_click_inside_board(mouse_pos):
    x, y = mouse_pos
    return 660 <= x <= 1260 and 241 <= y <= 839

def check_winner(board):
    # função que verifica se algum jogador já ganhou
    for row in board:
        if all([cell == 'X' for cell in row]) or all([cell == 'O' for cell in row]):
            return True

    for col in range(3):
        if all([board[row][col] == 'X' for row in range(3)]) or all([board[row][col] == 'O' for row in range(3)]):
            return True

    if (board[0][0] == board[1][1] == board[2][2] != '') or (board[0][2] == board[1][1] == board[2][0] != ''):
        return True

    return False

def start_game():
    board = [['', '', ''], ['', '', ''], ['', '', '']]
    current_player = 'X'
    
    game_running = True
    while game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if is_click_inside_board(event.pos):
                    row, col = get_clicked_cell(event.pos)
                    if board[row][col] == '':
                        board[row][col] = current_player
                        if check_winner(board):
                            return current_player
                        current_player = 'O' if current_player == 'X' else 'X'

        screen.fill((110, 92, 98))
        draw_hash()

        for row in range(3):
            for col in range(3):
                if board[row][col] == 'X':
                    draw_x((660 + col * 200 + 30, 241 + row * 200 + 30),
                           (660 + col * 200 + 170, 241 + row * 200 + 170),
                           (660 + col * 200 + 170, 241 + row * 200 + 30),
                           (660 + col * 200 + 30, 241 + row * 200 + 170))
                elif board[row][col] == 'O':
                    draw_circle((660 + col * 200 + 100, 241 + row * 200 + 100))

        if current_player == 'X':
            write('Vez de ', (327, 540), (255, 255, 255))
            write('X', (327 + 160, 540), (58, 163, 148))
        else:
            write('Vez de ', (1615, 540), (255, 255, 255))
            write('O', (1615 + 160, 540), (211, 173, 105))
        
        pygame.display.flip()

def winner_screen(winner):
    screen.fill((110, 92, 98))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                return 
            
        if winner == 'O':
            write('O venceu!', (960, 540), (255, 255, 255))
        else:
            write('X venceu!', (960, 540), (255, 255, 255))
        
        pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            winner = start_game()
            winner_screen(winner)

    screen.fill((110, 92, 98))
    draw_hash()
    draw_circle((960, 335))
    draw_circle((753, 540))
    draw_circle((1164, 540))
    draw_circle((960, 742))
    draw_x((682, 262), (831, 412), (680, 412), (830, 262))
    draw_x((1088, 262), (1237, 412), (1085, 412), (1235, 262))
    draw_x((888, 465), (1037, 615), (886, 615), (1035, 465))
    draw_x((831, 819), (680, 668), (680, 819), (831, 668))
    draw_x((1087, 668), (1237, 819), (1085, 819), (1235, 668))
    write('Toque em qualquer lugar para jogar!', (960, 972), (255, 255, 255))

    pygame.display.flip()
    pygame.time.Clock().tick(60)  

pygame.quit()
