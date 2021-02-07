import pygame, sys
from pygame.draw import *

# После импорта библиотеки, необходимо её инициализировать:
pygame.init()

FPS = 30
# И создать окно:
screen = pygame.display.set_mode((600, 480))


# здесь будут рисоваться фигуры
rect(screen, color=(212, 212, 212), rect=(0, 0, 600, 480))
# голова
circle(screen, color=(254, 254, 34), center=(300, 240), radius=120, width=0)
circle(screen, color=(0, 0, 0), center=(300, 240), radius=121, width=1)
# глаза
circle(screen, color=(0, 0, 0), center=(250, 200), radius=26, width=1)
circle(screen, color=(254, 34, 34), center=(250, 200), radius=25, width=0)
circle(screen, color=(0, 0, 0), center=(250, 200), radius=10, width=0)

circle(screen, color=(0, 0, 0), center=(350, 200), radius=22, width=1)
circle(screen, color=(254, 34, 34), center=(350, 200), radius=21, width=0)
circle(screen, color=(0, 0, 0), center=(350, 200), radius=10, width=0)

# рот
rect(screen, color=(0, 0, 0), rect=(240, 290, 120, 20))

# брови
polygon(screen, color=(0, 0, 0), points=((290, 190), (300, 180), (220, 140), (210, 150)))
polygon(screen, color=(0, 0, 0), points=((327, 190), (317, 185), (400, 140), (410, 145)))


# после чего, чтобы они отобразились на экране, экран нужно обновить:
pygame.display.update()
# Эту же команду нужно будет повторять, если на экране происходят изменения.

# Наконец, нужно создать основной цикл, в котором будут отслеживаться
# происходящие события.
# Пока единственное событие, которое нас интересует - выход из программы.
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True


sys.exit()