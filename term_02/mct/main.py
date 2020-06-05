import pygame
from math import sin, pi, radians
import numpy as np

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

fi = float(input("Input angle: "))
pygame.init()

sc = pygame.display.set_mode((500, 500))

ORANGE = (255, 150, 100)
GREEN = (124,252,0)
RED = (220,20,60)
BLUE = (30,144,255)

clock = pygame.time.Clock()

sc.fill(BLACK)
xss = [[i * 20 + 50 - 200 * pi, 20 * sin(i) + 200 + 50] for i in range(200)]

pygame.draw.arc(sc, RED, (0, 200, 100, 100), 3*pi/2, 2*pi, 50)
pygame.draw.arc(sc, ORANGE, (0, 200, 100, 100), 0, pi/2, 50)
pygame.draw.arc(sc, BLUE, (0, 200, 100, 100), pi/2, pi, 50)
pygame.draw.arc(sc, GREEN, (0, 200, 100, 100), pi, 3 * pi / 2, 50)
pygame.draw.aalines(sc, WHITE, False, xss)
pygame.display.update()

pygame.time.delay(1000)

x = 0
y = 0

fi = radians(fi)
count = 0
flag = True
k = 20
while True:
    clock.tick(5)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    if flag != True:
        x += pi/6
    else:
        x -= pi/6
    if x * k > 500 - 100:
        flag = True
    if x * k < 1:
        flag = False
    y = sin(x)


    sc.fill(BLACK)

    
    pygame.draw.arc(sc, GREEN, (x*k, 200 + y*k, 100, 100), pi + fi*count, 3 * pi / 2 + fi*count, 50)
    pygame.draw.arc(sc, ORANGE, (x*k, 200 + y*k, 100, 100), 0 + fi*count, pi / 2 + fi*count, 50)
    pygame.draw.arc(sc, BLUE, (x*k, 200 + y*k, 100, 100), pi / 2 + fi*count, pi + fi*count, 50)
    pygame.draw.arc(sc, RED, (x*k, 200 + y*k, 100, 100), 3 * pi / 2 + fi*count, 2 * pi + fi*count, 50)
    pygame.draw.aalines(sc, WHITE, False, xss)

    pygame.display.update()
    
    count -= 1

