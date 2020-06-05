import pygame
 
pygame.init()


def main():
    # Здесь определяются константы, классы и функции.
    FPS = 30
 
    # Здесь происходит инициация, создание объектов и др.
    sc = pygame.display.set_mode((600, 400))
    clock = pygame.time.Clock()
    
    # Ксли надо до цикла отобразить объекты на экране.
    pygame.display.update()

    # Главный цикл.
    while True:
        # Pадержка.
        clock.tick(FPS)

        # Цикл обработки событий.
        for event in pygame.event.get():
            # print()
            # print(event, end=' ')
            if event.type == pygame.QUIT:
                return

        # --------
        # Изменение объектов и многое др.
        # --------
    
        # Обновление экрана.      
        pygame.display.update()
        

if __name__ == "__main__":
    main()
