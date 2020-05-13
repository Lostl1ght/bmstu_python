from random import randint
import pygame
pygame.init()
 
sc = pygame.display.set_mode((400, 400))
 
background = pygame.Surface((400, 200))
background.fill((0, 255, 0))
xb = 0
yb = 100
 
hero = pygame.Surface((100, 100))
hero.fill((255, 0, 0))
x = 0
y = 50
 
# порядок прорисовки важен!
background.blit(hero, (x, y))
sc.blit(background, (xb, yb))
 
pygame.display.update()
 
while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
        elif i.type == pygame.MOUSEBUTTONUP:
            yb = randint(0, 200)
 
    if x < 400:
        x += 2
    else:
        x = 0
 
    sc.fill((0, 0, 0))
    background.fill((0, 255, 0))
 
    background.blit(hero, (x, y))
    sc.blit(background, (xb, yb))
 
    pygame.display.update()
 
    pygame.time.delay(30)