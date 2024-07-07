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

def start_game():
    game_running = True
    while game_running:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            return False

      screen.fill((110, 92, 98))
      draw_hash()
      write('Vez de ', (327, 540), (255, 255, 255))
      write('X', (327 + 160, 540), (58, 163, 148))
      pygame.display.flip()
        
    return True

running = True
while running:
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()
      elif event.type == pygame.MOUSEBUTTONDOWN:
          start_game()

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
  pygame.time.Clock().tick(60)  # Limita a 60 frames por segundo

pygame.quit()
