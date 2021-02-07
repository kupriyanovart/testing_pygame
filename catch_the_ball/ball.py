from pygame.draw import *
import math
from random import randint
from catch_the_ball.config import *


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