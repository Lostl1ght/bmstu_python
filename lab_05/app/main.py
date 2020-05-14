from random import randint
import pygame


class Car:
    EMPTY = pygame.Color(0, 0, 0, 0)
    l = 1
    tick = 0

    def __init__(self, x, y, car_images, crash_images):
        self.car = pygame.image.load(car_images + '\car.png').convert_alpha()

        self.base_surf = pygame.Surface((self.car.get_width(),
                                         self.car.get_height()), flags=pygame.SRCALPHA)
        self.base_surf_rect = self.base_surf.get_rect(topleft=(x, y))

        self.wheel1 = [pygame.image.load(car_images + '\wheel1.png').convert_alpha(),
                       pygame.image.load(car_images + '\wheel2.png').convert_alpha()]
        self.wheel1_rect = [self.wheel1[0].get_rect(center=(40, 75)),
                            self.wheel1[1].get_rect(center=(40, 75))]

        self.wheel2 = [pygame.image.load(car_images + '\wheel1.png').convert_alpha(),
                       pygame.image.load(car_images + '\wheel2.png').convert_alpha()]
        self.wheel2_rect = [self.wheel2[0].get_rect(center=(170, 75)),
                            self.wheel2[1].get_rect(center=(170, 75))]

        self.crash = [pygame.image.load(crash_images + '\crash1.png').convert_alpha(),
                      pygame.image.load(crash_images + '\crash2.png').convert_alpha()]
        self.crash_rect = [self.crash[0].get_rect(), self.crash[1].get_rect()]

        self.base_surf.fill(self.EMPTY)
        self.base_surf.blit(self.car, (0, 0))
        self.base_surf.blit(self.wheel1[0], self.wheel1_rect[0])

    def move(self):        
        car.base_surf_rect.x += 5
        self.base_surf.fill(self.EMPTY)

        self.base_surf.blit(self.car, (0, 0))
        self.base_surf.blit(self.wheel2[self.l], self.wheel2_rect[self.l])
        self.base_surf.blit(self.wheel1[self.l], self.wheel1_rect[self.l])
        self.l = (self.l + 1) % 2

    def burn(self):        
        self.tick += 1
        if self.tick != 6:
            return
        self.tick = 0
        
        self.base_surf.fill(self.EMPTY)

        self.base_surf.blit(self.crash[self.l], self.crash_rect[self.l])
        self.l = (self.l + 1) % 2


pygame.init()
W = 500
H = 200
WHITE = (255, 255, 255)
DIST = 300

sc = pygame.display.set_mode((W, H))

bg = pygame.Surface((W, H))
bg_rect = bg.get_rect()

car = Car(0, 90, 'moving_car', 'car_crash')

bg.fill(WHITE)
bg.blit(car.base_surf, car.base_surf_rect)
sc.blit(bg, bg_rect)

pygame.display.update()

while True:
    pygame.time.delay(100)

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()

    sc.fill(WHITE)
    bg.fill(WHITE)

    if car.base_surf_rect.x < DIST - car.car.get_width():
        car.move()
    else:
        car.burn()

    bg.blit(car.base_surf, car.base_surf_rect)
    sc.blit(bg, bg_rect)

    pygame.display.update()
