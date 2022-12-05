import pygame

pygame.display.set_caption('Что-то')
runGame = True


def game():
    global runGame
    pygame.init()
    screen = pygame.display.set_mode(size)

    while runGame:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runGame = False
        screen.fill((0, 0, 0))
        pygame.display.flip()

        pass
    pygame.quit()


try:
    w, n = list(map(int, input().split()))
    size = w * n * 2, w * n * 2
    if type(w).__name__ != 'int' or type(n).__name__ != 'int':
        raise ValueError
    game()
except ValueError:
    print('Неправильный формат ввода')

