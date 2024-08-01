import pygame
import sys
import time

pygame.init()
pygame.font.init()

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 600
CELL_SIZE = 200
BOARD_START_X = 660
BOARD_START_Y = 241

font = pygame.font.Font('Mitr-Bold.ttf', 40)
small_font = pygame.font.Font('Mitr-Bold.ttf', 50)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Jogo da Velha Infinito')

def draw_hash():
    lines = [
        ((447, 108), (447, 492)),
        ((576, 108), (576, 492)),
        ((320, 236), (704, 236)),
        ((320, 364), (704, 364)),
    ]
    for line in lines:
        pygame.draw.line(screen, (97, 84, 88), line[0], line[1], 9)

def draw_circle(coord, highlight=False):
    color = (161, 133, 102) if highlight else (211, 173, 105)
    pygame.draw.circle(screen, color, coord, 50, 15)

def draw_x(coord1, coord2, coord3, coord4, highlight=False):
    color = (84, 128, 123) if highlight else (58, 163, 148)
    pygame.draw.line(screen, color, coord1, coord2, 25)
    pygame.draw.line(screen, color, coord3, coord4, 25)

def write(phrase, coord, color, font=font):
    text = font.render(phrase, True, color)
    text_rect = text.get_rect(center=coord)
    screen.blit(text, text_rect)

def get_clicked_cell(mouse_pos):
    x, y = mouse_pos
    if BOARD_START_X <= x <= BOARD_START_X + 3 * CELL_SIZE and BOARD_START_Y <= y <= BOARD_START_Y + 3 * CELL_SIZE:
        return (y - BOARD_START_Y) // CELL_SIZE, (x - BOARD_START_X) // CELL_SIZE
    return None

def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != '' or board[0][i] == board[1][i] == board[2][i] != '':
            return True
    if board[0][0] == board[1][1] == board[2][2] != '' or board[0][2] == board[1][1] == board[2][0] != '':
        return True
    return False

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
                        if len(moves[current_player]) < 3:
                            moves[current_player].append((row, col))
                        else:
                            old_row, old_col = moves[current_player].pop(0)
                            board[old_row][old_col] = ''
                            moves[current_player].append((row, col))
                        board[row][col] = current_player
                        if check_winner(board):
                            end_time = time.time()
                            return current_player, end_time - start_time
                        current_player = 'O' if current_player == 'X' else 'X'

        screen.fill((110, 92, 98))
        draw_hash()

        for row in range(3):
            for col in range(3):
                if board[row][col] == 'X':
                    highlight = (row, col) == moves['X'][0] if len(moves['X']) == 3 and current_player == 'X' else False
                    draw_x(
                        (BOARD_START_X + col * CELL_SIZE + 30, BOARD_START_Y + row * CELL_SIZE + 30),
                        (BOARD_START_X + col * CELL_SIZE + 170, BOARD_START_Y + row * CELL_SIZE + 170),
                        (BOARD_START_X + col * CELL_SIZE + 170, BOARD_START_Y + row * CELL_SIZE + 30),
                        (BOARD_START_X + col * CELL_SIZE + 30, BOARD_START_Y + row * CELL_SIZE + 170),
                        highlight
                    )
                elif board[row][col] == 'O':
                    highlight = (row, col) == moves['O'][0] if len(moves['O']) == 3 and current_player == 'O' else False
                    draw_circle((BOARD_START_X + col * CELL_SIZE + 100, BOARD_START_Y + row * CELL_SIZE + 100), highlight)


        if current_player == 'X':
            write('Vez de ', (150, 300), (255, 255, 255))
            write('X', (150 + 85, 300), (58, 163, 148))
        else:
            write('Vez de ', (875, 300), (255, 255, 255))
            write('O', (875 + 85, 300), (211, 173, 105))
        
        pygame.display.flip()



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
            write('X venceu!', (960, 440), (58, 163, 148))
        else:
            write('O venceu!', (960, 440), (211, 173, 105))
            
        minutes = int(game_duration) // 60
        seconds = int(game_duration) % 60
        time_text = f'Duração do jogo: {minutes}:{seconds:02d}'

        write(time_text, (960, 640), (255, 255, 255), small_font)
        pygame.display.flip()

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
        draw_circle((512, 169))
        draw_circle((381, 300))
        draw_circle((641, 300))
        draw_circle((512, 429))
        draw_x((340, 128), (422, 210), (422, 128), (340, 210))
        draw_x((600, 128), (682, 210), (682, 128), (600, 210))
        draw_x((471, 258), (553, 341), (553, 258), (471, 341))
        draw_x((340, 388), (422, 470), (422, 388), (340, 470))
        draw_x((600, 388), (682, 470), (682, 388), (600, 470))
        write('Toque em qualquer lugar para jogar!', (512, 540), (255, 255, 255))

        pygame.display.flip()
        pygame.time.Clock().tick(60)  

    pygame.quit()

if __name__ == "__main__":
    main()
