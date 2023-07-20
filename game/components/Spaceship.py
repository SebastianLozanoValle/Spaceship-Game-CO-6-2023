import pygame
from game.utils.constants import SPACESHIP, SCREEN_WIDTH, SCREEN_HEIGHT, BULLET_PLAYER_TYPE, SPACESHIP_SHIELD
from game.components.power_ups.shield import Shield


class Spaceship:

    WIDTH = 40
    HEIGHT = 60
    X_POS = (SCREEN_WIDTH // 2) - WIDTH
    Y_POS = 500
    SHOOTING_TIME = 5

    def __init__(self):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.is_alive = True
        self.shooting_time = 0
        self.has_shield = False
        self.time_up = 0

    def update(self, game_speed, user_input, bullet_handler):
        self.shooting_time += 1
        if user_input[pygame.K_LEFT]:
            self.move_left(game_speed)

        elif user_input[pygame.K_RIGHT]:
            self.move_rigth(game_speed)

        elif user_input[pygame.K_UP]:
            self.move_up(game_speed)

        elif user_input[pygame.K_DOWN]:
            self.move_down(game_speed)

        if user_input[pygame.K_SPACE]:
            self.shoot(bullet_handler)

        if self.has_shield:
            time_to_show = round((self.time_up - pygame.time.get_ticks())/1000, 2)
            if time_to_show < 0:
                self.deactivate_power_up()

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def move_left(self, game_speed):
        self.rect.x -= game_speed
        if self.rect.x <= 0:
            self.rect.x = (SCREEN_WIDTH - self.WIDTH)

    def move_rigth(self, game_speed):
        self.rect.x += game_speed
        if self.rect.x >= (SCREEN_WIDTH - self.WIDTH):
            self.rect.x = 0
        

    def move_up(self, game_speed):
        if self.rect.y >= (SCREEN_HEIGHT//2):
            self.rect.y -= game_speed

    def move_down(self, game_speed):
        if self.rect.y <= (SCREEN_HEIGHT - self.HEIGHT):
            self.rect.y += game_speed

    def shoot(self, bullet_handler):
        if self.shooting_time % self.SHOOTING_TIME == 0:
            bullet_handler.add_bullet(BULLET_PLAYER_TYPE, self.rect.center)

    def active_power_up(self, power_up):
        self.time_up = power_up.time_up
        if type(power_up) == Shield:
            self.image = SPACESHIP_SHIELD
            self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
            self.has_shield = True

    def deactivate_power_up(self):
        self.has_shield = False
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))

    def reset(self):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.is_alive = True
        self.shooting_time = 0
        self.has_shield = False