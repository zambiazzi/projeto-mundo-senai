import pygame
import sys
import time

# Inicialização do Pygame
pygame.init()

# Configurações da janela
screen_width = 1920
screen_height = 1080
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Jogo da Velha")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Fontes
font = pygame.font.SysFont(None, 75)
small_font = pygame.font.SysFont(None, 50)

# Variáveis de animação
animation_index = 0
animation_symbols = ['X', 'O']
animation_time = 500  # milissegundos

# Variáveis do jogo
board = [['' for _ in range(3)] for _ in range(3)]
current_player = 'X'
moves = {'X': [], 'O': []}
game_over = False
start_time = None

# Função para desenhar a cerquilha
def draw_grid():
    for i in range(1, 3):
        pygame.draw.line(screen, BLACK, (screen_width // 2 - 150, screen_height // 2 - 150 + i * 100),
                         (screen_width // 2 + 150, screen_height // 2 - 150 + i * 100), 5)
        pygame.draw.line(screen, BLACK, (screen_width // 2 - 150 + i * 100, screen_height // 2 - 150),
                         (screen_width // 2 - 150 + i * 100, screen_height // 2 + 150), 5)

# Função para desenhar a mensagem inicial
def draw_initial_message():
    message = "Clique em qualquer lugar para jogar!"
    text = small_font.render(message, True, BLACK)
    screen.blit(text, (screen_width // 2 - text.get_width() // 2, screen_height // 2 + 200))

# Função para desenhar a animação inicial
def draw_animation():
    global animation_index
    symbol = animation_symbols[animation_index]
    for row in range(3):
        for col in range(3):
            text = font.render(symbol, True, RED if symbol == 'X' else BLUE)
            screen.blit(text, (screen_width // 2 - 150 + col * 100 + 25, screen_height // 2 - 150 + row * 100 + 25))
    animation_index = (animation_index + 1) % 2

# Função para desenhar o estado do tabuleiro
def draw_board():
    for row in range(3):
        for col in range(3):
            if board[row][col] != '':
                text = font.render(board[row][col], True, RED if board[row][col] == 'X' else BLUE)
                screen.blit(text, (screen_width // 2 - 150 + col * 100 + 25, screen_height // 2 - 150 + row * 100 + 25))

# Função para desenhar a mensagem de quem é a vez
def draw_turn_message():
    message = f"Vez de {current_player}"
    text = small_font.render(message, True, BLACK)
    screen.blit(text, (screen_width // 2 - 200, screen_height // 2 - 250))

# Função para verificar se alguém venceu
def check_win():
    global game_over
    for row in board:
        if row[0] == row[1] == row[2] != '':
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != '':
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != '':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != '':
        return board[0][2]
    return ''

# Função para desenhar a mensagem de vitória
def draw_win_message(winner):
    screen.fill(WHITE)
    message = f"{winner} venceu!"
    text = font.render(message, True, BLACK)
    screen.blit(text, (screen_width // 2 - text.get_width() // 2, screen_height // 2 - 100))
    elapsed_time = int(time.time() - start_time)
    minutes, seconds = divmod(elapsed_time, 60)
    time_message = f"Tempo de jogo: {minutes}:{seconds:02d}"
    time_text = small_font.render(time_message, True, BLACK)
    screen.blit(time_text, (screen_width // 2 - time_text.get_width() // 2, screen_height // 2))
    button_message = "Voltar ao menu"
    button_text = small_font.render(button_message, True, BLACK)
    screen.blit(button_text, (screen_width // 2 - button_text.get_width() // 2, screen_height // 2 + 100))
    return pygame.Rect(screen_width // 2 - button_text.get_width() // 2, screen_height // 2 + 100, button_text.get_width(), button_text.get_height())

# Função principal do jogo
def main():
    global animation_index, current_player, game_over, start_time
    running = True
    game_started = False
    last_update = pygame.time.get_ticks()
    button_rect = None

    while running:
        screen.fill(WHITE)
        draw_grid()

        if not game_started:
            draw_animation()
            draw_initial_message()
            if pygame.time.get_ticks() - last_update > animation_time:
                last_update = pygame.time.get_ticks()
                animation_index = (animation_index + 1) % 2
        else:
            if game_over:
                winner = check_win()
                button_rect = draw_win_message(winner)
            else:
                draw_board()
                draw_turn_message()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not game_started:
                    game_started = True
                    start_time = time.time()
                    board[:] = [['' for _ in range(3)] for _ in range(3)]
                    current_player = 'X'
                    moves = {'X': [], 'O': []}
                    game_over = False
                elif game_over and button_rect and button_rect.collidepoint(event.pos):
                    game_started = False
                elif not game_over:
                    x, y = event.pos
                    row = (y - (screen_height // 2 - 150)) // 100
                    col = (x - (screen_width // 2 - 150)) // 100
                    if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == '':
                        if len(moves[current_player]) < 3:
                            board[row][col] = current_player
                            moves[current_player].append((row, col))
                        else:
                            old_move = moves[current_player].pop(0)
                            board[old_move[0]][old_move[1]] = ''
                            board[row][col] = current_player
                            moves[current_player].append((row, col))
                        winner = check_win()
                        if winner:
                            game_over = True
                        else:
                            current_player = 'O' if current_player == 'X' else 'X'

        pygame.display.flip()
        pygame.time.Clock().tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
