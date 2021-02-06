import pygame
import math
from pygame.draw import *
from random import randint
pygame.init()

FPS = 1
screen = pygame.display.set_mode((1100, 600))

# Размеры игрового поля
FIELD_SIZE_X = 800
FIELD_SIZE_Y = 600
# Минимальный и максимальный радиус шара
MIN_RADIUS = 20
MAX_RADIUS = 100

WHITE = (240, 240, 230)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


class Ball:
    """
    Создает объект шарик
    Центр шара в точке (x, y) - > Выбираются случайно
    Радиус шара r выбирается случайно
    Цвет шара color выбирается случайно
    """
    def __init__(self):
        self.x = randint(MAX_RADIUS, FIELD_SIZE_X - MAX_RADIUS)
        self.y = randint(MAX_RADIUS, FIELD_SIZE_Y - MAX_RADIUS)
        self.r = randint(MIN_RADIUS, MAX_RADIUS)
        self.color = COLORS[randint(0, len(COLORS) - 1)]

    def draw(self, screen):
        """Рисует шарик на экране"""
        circle(screen, self.color, (self.x, self.y), self.r)

    def _get_distance_between_click_and_ball_center(self, event):
        return math.sqrt((event.pos[0] - self.x) ** 2 + (event.pos[1] - self.y) ** 2)

    def clicked(self, event):
        """Возвращает True если на шарик кликнули мышкой, иначе False"""
        return self.r >= self._get_distance_between_click_and_ball_center(event)



clock = pygame.time.Clock()
finished = False
game_field = pygame.Rect(0, 0, FIELD_SIZE_X, FIELD_SIZE_Y)

screen.fill(WHITE)
screen.fill(BLACK, game_field)

pygame.display.update()
ball = Ball()
ball.draw(screen=screen)

while not finished:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if ball.clicked(event):
                print('YOU GOT IT!!')
            else:
                print('MISS!!')

    screen.fill(BLACK, game_field)
    ball = Ball()
    ball.draw(screen=screen)
    pygame.display.update()

pygame.quit()
