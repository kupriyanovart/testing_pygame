from catch_the_ball.ball import Ball
from catch_the_ball.config import *
import pygame


def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_SIZE_X, WINDOW_SIZE_Y))
    clock = pygame.time.Clock()

    game = MainGame(screen, clock)
    game.start()


def show_information(screen, score, lives):
    pygame.font.init()
    my_font = pygame.font.Font(None, 30)
    text_score = my_font.render(f"Score:{score}", True, RED)
    text_level = my_font.render(f'Level: {level}', True, RED)
    text_lives = my_font.render(f'Lives: {lives}', True, RED)
    screen.blit(text_score, (FIELD_SIZE_X + 20, 20))
    screen.blit(text_level, (FIELD_SIZE_X + 20, 60))
    screen.blit(text_lives, (FIELD_SIZE_X + 20, 100))


class MainGame:
    def __init__(self, screen, clock):
        self.screen = screen
        self.finished = False
        self.clock = clock
        self.game_field = pygame.Rect(0, 0, FIELD_SIZE_X, FIELD_SIZE_Y)
        self.menu_filed = pygame.Rect(FIELD_SIZE_X, 0, WINDOW_SIZE_X, WINDOW_SIZE_Y)
        self.score = score
        self.lives = lives
        self.level = level

    def game_over(self):
        pygame.font.init()
        my_font = pygame.font.Font(None, 50)
        text_game_over = my_font.render("GAME OVER!", True, RED)
        text_score = my_font.render(f'Your score is {self.score}', True, RED)
        self.screen.fill(WHITE, self.menu_filed)
        self.screen.fill(BLACK, self.game_field)
        self.screen.blit(text_game_over, (FIELD_SIZE_X + 20, FIELD_SIZE_Y // 2))
        self.screen.blit(text_score, (FIELD_SIZE_X + 20, FIELD_SIZE_Y // 2 + 70))
        pygame.display.update()
        while not self.finished:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.finished = True

    def start(self):
        self.screen.fill(WHITE, self.menu_filed)
        self.screen.fill(BLACK, self.game_field)
        pygame.display.update()
        ball = Ball()
        ball.draw(screen=self.screen)

        while not self.finished:
            self.clock.tick(FPS * (self.level / 2))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.finished = True
                elif self.lives <= 0:
                    self.game_over()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if ball.clicked(event):
                        if not ball.is_clicked:
                            self.score += point_for_ball * self.level
                            ball.is_clicked = True
                    else:
                        self.lives -= 1

            self.screen.fill(BLACK, self.game_field)
            self.screen.fill(WHITE, self.menu_filed)
            ball = Ball()
            ball.draw(screen=self.screen)
            show_information(self.screen, self.score, self.lives)
            pygame.display.update()

            if self.score > 50 and self.level == 1:
                self.level += 1
            elif self.score > 500 and self.level == 2:
                self.level += 1

        pygame.quit()


if __name__ == '__main__':
    main()
