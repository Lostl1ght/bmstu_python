from random import randint
import pygame


class Car:
    EMPTY = pygame.Color(0, 0, 0, 0)
    IMG = 1
    TICK = 5

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
        self.base_surf_rect.x += 5
        self.base_surf.fill(self.EMPTY)

        self.base_surf.blit(self.car, (0, 0))
        self.base_surf.blit(self.wheel2[self.IMG], self.wheel2_rect[self.IMG])
        self.base_surf.blit(self.wheel1[self.IMG], self.wheel1_rect[self.IMG])
        self.IMG = (self.IMG + 1) % 2

    def burn(self):
        self.TICK += 1
        if self.TICK != 6:
            return
        self.TICK = 0

        self.base_surf.fill(self.EMPTY)

        self.base_surf.blit(self.crash[self.IMG], self.crash_rect[self.IMG])
        self.IMG = (self.IMG + 1) % 2


class Man:
    EMPTY = pygame.Color(0, 0, 0, 0)
    IMG = 1
    TICK = -7

    def __init__(self, x, y, man_images):
        self.man = pygame.image.load(man_images + '\stand.png').convert_alpha()

        self.base_surf = pygame.Surface((self.man.get_width(),
                                         self.man.get_height()), flags=pygame.SRCALPHA)
        self.base_surf_rect = self.base_surf.get_rect(topleft=(x, y))

        self.ahead = [pygame.image.load(man_images + '\_ahead1.png').convert_alpha(),
                      pygame.image.load(man_images + '\_ahead2.png').convert_alpha()]
        self.ahead_rect = [self.ahead[0].get_rect(),
                           self.ahead[1].get_rect()]

        self.left = [pygame.image.load(man_images + '\left1.png').convert_alpha(),
                     pygame.image.load(man_images + '\left2.png').convert_alpha()]
        self.left_rect = [self.left[0].get_rect(),
                          self.left[1].get_rect()]

        self.right = [pygame.image.load(man_images + '\_right1.png').convert_alpha(),
                      pygame.image.load(man_images + '\_right2.png').convert_alpha()]
        self.right_rect = [self.right[0].get_rect(),
                           self.right[1].get_rect()]
        

        self.scratch = [pygame.image.load(man_images + '\scratch1.png').convert_alpha(),
                      pygame.image.load(man_images + '\scratch2.png').convert_alpha()]
        self.scratch_rect = [self.scratch[0].get_rect(),
                             self.scratch[1].get_rect()]

    def place(self):
        if self.TICK != 4:
            return
        self.base_surf.fill(self.EMPTY)
        self.base_surf.blit(self.man, (0, 0))

    def move_left(self, dist):
        if self.TICK != 8:
            return
        if self.base_surf_rect.x < dist:
            return
        self.base_surf_rect.x -= 10
        self.TICK = 5
        self.base_surf.fill(self.EMPTY)
        self.base_surf.blit(self.left[self.IMG], self.left_rect[self.IMG])
        self.IMG = (self.IMG + 1) % 2

    def move_ahead(self):
        if self.TICK != 12 and self.TICK != 15:
            return

        self.base_surf.fill(self.EMPTY)
        self.base_surf.blit(self.ahead[self.IMG], self.ahead_rect[self.IMG])
        self.IMG = (self.IMG + 1) % 2

    def move_right(self, dist):
        if self.TICK != 19:
            return
        if self.base_surf_rect.x > dist:
            return
        self.base_surf_rect.x += 10
        self.TICK = 16
        self.base_surf.fill(self.EMPTY)
        self.base_surf.blit(self.right[self.IMG], self.right_rect[self.IMG])
        self.IMG = (self.IMG + 1) % 2

    def do_scratch(self):        
        if self.TICK != 24 and self.TICK != 20:
            return
        
        self.TICK = 21
        self.base_surf.fill(self.EMPTY)
        self.base_surf.blit(self.scratch[self.IMG], self.scratch_rect[self.IMG])
        self.IMG = (self.IMG + 1) % 2



pygame.init()
W = 865
H = 260
WHITE = (255, 255, 255)
DIST = 500

sc = pygame.display.set_mode((W, H))

bg = pygame.Surface((W, H))
bg_rect = bg.get_rect()

road = pygame.image.load('bg.png').convert_alpha()
road_rect = road.get_rect()

car = Car(0, 90, 'moving_car', 'car_crash')
man = Man(DIST - car.car.get_width() + 90, 90, 'walk')

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
        bg.blit(car.base_surf, car.base_surf_rect)
        sc.blit(bg, bg_rect)
    else:
        car.burn()

        man.TICK += 1
        man.place()
        man.move_left(DIST - car.car.get_width() - 35)
        man.move_ahead()
        man.move_right(DIST - car.car.get_width() + 60)
        man.do_scratch()

        
        if man.TICK < 16:
            bg.blit(man.base_surf, man.base_surf_rect)
            bg.blit(car.base_surf, car.base_surf_rect)
        else:
            bg.blit(car.base_surf, car.base_surf_rect)
            bg.blit(man.base_surf, man.base_surf_rect)

        sc.blit(bg, bg_rect)

    pygame.display.update()
