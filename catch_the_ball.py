import pygame
import math
from pygame.draw import *
from random import randint
pygame.init()

# Размеры окна
WINDOW_SIZE_X = 1100
WINDOW_SIZE_Y = 600

FPS = 1

screen = pygame.display.set_mode((WINDOW_SIZE_X, WINDOW_SIZE_Y))

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

score = 0
level = 1
point_for_ball = 10


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
        self.is_clicked = False

    def draw(self, screen):
        """Рисует шарик на экране"""
        circle(screen, self.color, (self.x, self.y), self.r)

    def _get_distance_between_click_and_ball_center(self, event):
        return math.sqrt((event.pos[0] - self.x) ** 2 + (event.pos[1] - self.y) ** 2)

    def clicked(self, event):
        """Возвращает True если на шарик кликнули мышкой, иначе False"""
        return self.r >= self._get_distance_between_click_and_ball_center(event)


def show_inforation(score, screen):
    pygame.font.init()
    my_font = pygame.font.Font(None, 30)
    text_score = my_font.render(f"Score:{score}", True, RED)
    text_level = my_font.render(f'Level: {level}', True, RED)
    screen.blit(text_score, (FIELD_SIZE_X + 20, 20))
    screen.blit(text_level, (FIELD_SIZE_X + 20, 60))


clock = pygame.time.Clock()
finished = False
game_field = pygame.Rect(0, 0, FIELD_SIZE_X, FIELD_SIZE_Y)
menu_filed = pygame.Rect(FIELD_SIZE_X, 0, WINDOW_SIZE_X, WINDOW_SIZE_Y)

screen.fill(WHITE, menu_filed)
screen.fill(BLACK, game_field)

pygame.display.update()
ball = Ball()
ball.draw(screen=screen)

while not finished:
    clock.tick(FPS * (level / 2))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if ball.clicked(event):
                if not ball.is_clicked:
                    score += point_for_ball * level
                    ball.is_clicked = True

    screen.fill(BLACK, game_field)
    screen.fill(WHITE, menu_filed)
    ball = Ball()
    ball.draw(screen=screen)
    show_inforation(score, screen)
    pygame.display.update()

    if score > 50 and level == 1:
        level += 1
    elif score > 500 and level == 2:
        level += 1
pygame.quit()
