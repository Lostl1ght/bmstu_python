import pygame
pygame.init()
 
sc = pygame.display.set_mode((300, 300))
sc.fill((200, 255, 200))
 
surf2 = pygame.Surface((100, 100))
surf2.fill((255, 255, 255))  # белая
 
rect = surf2.get_rect()  # создается Rect
 
print(surf2.get_width())  # вывод 100
print(rect.width)  # 100
print(rect.x, rect.y)  # 0 0
 
sc.blit(surf2, rect)
pygame.display.update()
 
while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
 
    rect.x += 1
 
    sc.fill((200, 255, 200))
    sc.blit(surf2, rect)
    pygame.display.update()
 
    pygame.time.delay(20)