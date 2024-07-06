import pygame

pygame.init()

SCREEN_WIDTH = 1920
SCREEN_HIGHT = 1000

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HIGHT))
pygame.display.set_caption('Jogo da Velha')
screen.fill((110, 92, 98))

def drawHash():
  pygame.draw.line(screen, (97, 84, 88), (859, 241), (859, 839), 9)
  pygame.draw.line(screen, (97, 84, 88), (1059, 241), (1059, 839), 9)
  pygame.draw.line(screen, (97, 84, 88), (660, 440), (1260, 440), 9)
  pygame.draw.line(screen, (97, 84, 88), (660, 641), (1260, 641), 9)

def drawCircle(coordinate):
  pygame.draw.circle(screen, (211, 173, 105), coordinate, 75, 15)

def drawX(coordinate1, coordinate2, coordinate3, coordinate4):
  pygame.draw.line(screen, (58, 163, 148), coordinate1, coordinate2, 25)
  pygame.draw.line(screen, (58, 163, 148), coordinate3, coordinate4, 25)

run = True
while run:

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
  
  drawHash()
  drawCircle((960, 335))
  drawCircle((753, 540))
  drawCircle((1164, 540))
  drawCircle((960, 742))
  drawX((680, 262), (831, 412), (680, 412), (831, 262))
  drawX((1085, 262), (1237, 412), (1085, 412), (1237, 262))
  drawX((886, 465), (1037, 615), (886, 615), (1037, 465))
  drawX((831, 819), (680, 668), (680, 819), (831, 668))
  drawX((1085, 668), (1237, 819), (1085, 819), (1237, 668))

  pygame.display.flip()

pygame.quit()