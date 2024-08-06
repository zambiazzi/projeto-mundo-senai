import pygame
import sys
import time

pygame.init()
pygame.font.init()
pygame.mixer.init()

# definindo tamanhos
SCREEN_WIDTH = 1900
SCREEN_HEIGHT = 1080
CELL_SIZE = 200
BOARD_START_X = 660
BOARD_START_Y = 241

# configurações padrões
font = pygame.font.Font('Mitr-Bold.ttf', 74)
small_font = pygame.font.Font('Mitr-Bold.ttf', 50)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Jogo da Velha Infinito')
pygame.mouse.set_visible(False)
move_sound = pygame.mixer.Sound('play_sound.mp3')
win_sound = pygame.mixer.Sound('winning_sound.mp3')

# desenhar Serquilha
def draw_hash():
    lines = [
        ((859, 241), (859, 839)),
        ((1059, 241), (1059, 839)),
        ((660, 440), (1260, 440)),
        ((660, 641), (1260, 641)),
    ]
    for line in lines:
        pygame.draw.line(screen, (97, 84, 88), line[0], line[1], 9)

# desenhar O
def draw_circle(coord, highlight=False):
    color = (161, 133, 102) if highlight else (211, 173, 105)
    pygame.draw.circle(screen, color, coord, 75, 15)

# desenhar X
def draw_x(coord1, coord2, coord3, coord4, highlight=False):
    color = (84, 128, 123) if highlight else (58, 163, 148)
    pygame.draw.line(screen, color, coord1, coord2, 25)
    pygame.draw.line(screen, color, coord3, coord4, 25)

# escrever na tela
def write(phrase, coord, color, font=font):
    text = font.render(phrase, True, color)
    text_rect = text.get_rect(center=coord)
    screen.blit(text, text_rect)

# função que retorna as coordenadas da célula clicada
def get_clicked_cell(mouse_pos):
    x, y = mouse_pos
    if BOARD_START_X <= x <= BOARD_START_X + 3 * CELL_SIZE and BOARD_START_Y <= y <= BOARD_START_Y + 3 * CELL_SIZE:
        return (y - BOARD_START_Y) // CELL_SIZE, (x - BOARD_START_X) // CELL_SIZE
    return None

# função para verificar se algum jogador já ganhou
def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != '' or board[0][i] == board[1][i] == board[2][i] != '':
            return True
    if board[0][0] == board[1][1] == board[2][2] != '' or board[0][2] == board[1][1] == board[2][0] != '':
        return True
    return False

# lógica geral do jogo
def start_game():
    board = [[''] * 3 for _ in range(3)]
    moves = {'X': [], 'O': []}
    current_player = 'X'
    game_running = True
    start_time = time.time()
    
    while game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                cell = get_clicked_cell(event.pos)
                if cell:
                    row, col = cell
                    if board[row][col] == '':
                        move_sound.play()
                        
                        if len(moves[current_player]) < 3:
                            moves[current_player].append((row, col))
                        else:
                            old_row, old_col = moves[current_player].pop(0)
                            board[old_row][old_col] = ''
                            moves[current_player].append((row, col))
                        board[row][col] = current_player
                        if check_winner(board):
                            win_sound.play()
                            end_time = time.time()
                            return current_player, end_time - start_time
                        current_player = 'O' if current_player == 'X' else 'X'

        screen.fill((110, 92, 98))
        draw_hash()

        for row in range(3):
            for col in range(3):
                if board[row][col] == 'X':
                    highlight = (row, col) == moves['X'][0] if len(moves['X']) == 3 and current_player == 'X' else False
                    draw_x((BOARD_START_X + col * CELL_SIZE + 30, BOARD_START_Y + row * CELL_SIZE + 30),
                           (BOARD_START_X + col * CELL_SIZE + 170, BOARD_START_Y + row * CELL_SIZE + 170),
                           (BOARD_START_X + col * CELL_SIZE + 170, BOARD_START_Y + row * CELL_SIZE + 30),
                           (BOARD_START_X + col * CELL_SIZE + 30, BOARD_START_Y + row * CELL_SIZE + 170),
                           highlight)
                elif board[row][col] == 'O':
                    highlight = (row, col) == moves['O'][0] if len(moves['O']) == 3 and current_player == 'O' else False
                    draw_circle((BOARD_START_X + col * CELL_SIZE + 100, BOARD_START_Y + row * CELL_SIZE + 100),
                                highlight)

        if current_player == 'X':
            write('Vez de ', (327, 540), (255, 255, 255))
            write('X', (327 + 160, 540), (58, 163, 148))
        else:
            write('Vez de ', (1615, 540), (255, 255, 255))
            write('O', (1615 + 160, 540), (211, 173, 105))
        
        pygame.display.flip()

# tela do vencedor
def winner_screen(winner, game_duration):
    screen.fill((110, 92, 98))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                return 

        if winner == 'X':
            write('X ', (840, 440), (58, 163, 148))
            write('venceu!', (840 + 180, 440), (255, 255, 255))
        else:
            write('O ', (840, 440), (211, 173, 105))
            write('venceu!', (840 + 180, 440), (255, 255, 255))
            
        minutes = int(game_duration) // 60
        seconds = int(game_duration) % 60
        time_text = f'Tempo de jogo: {minutes}:{seconds:02d}'

        write(time_text, (960, 640), (255, 255, 255), small_font)
        pygame.display.flip()

# loop principal
def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                winner, game_duration = start_game()
                winner_screen(winner, game_duration)

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

if __name__ == "__main__":
    main()
