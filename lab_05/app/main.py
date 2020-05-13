from random import randint
import pygame
pygame.init()
W = 600
H = 100
WHITE = (255, 255, 255)
 
 
sc = pygame.display.set_mode((W, H))

surf = pygame.Surface((231,96))
surf_rect = surf.get_rect()
 
car = pygame.image.load('Car\car.png').convert_alpha()


wheel1 = [pygame.image.load('Car\wheel1.png').convert_alpha(), pygame.image.load('Car\wheel2.png').convert_alpha()]
wheel1_rect = [wheel1[0].get_rect(center=(40, 70)), wheel1[1].get_rect(center=(40, 70))]
 
sc.fill(WHITE)
surf.fill(WHITE)

surf.blit(car, (0, 0))
surf.blit(wheel1[0], wheel1_rect[0])
sc.blit(surf, surf_rect)


pygame.display.update()
l = 1
 
while True:    
    pygame.time.delay(50)

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()

    sc.fill(WHITE)
    surf.fill(WHITE)

    surf.blit(car, (0, 0))
    surf.blit(wheel1[l], wheel1_rect[l])
    sc.blit(surf, surf_rect)
    l += 1
    l %= 2


    if surf_rect.x < W - 150:
        surf_rect.x += 5
    else:
        surf_rect.x = 0
    
    pygame.display.update()