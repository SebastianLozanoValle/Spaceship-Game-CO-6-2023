import pygame

from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE
from game.components.Spaceship import Spaceship
from game.components.enemies.enemy_handler import EnemyHandler
from game.components.bullets.bullet_handler import BulletHandler
from game.utils import text_utils

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.player = Spaceship()
        self.enemy_handler = EnemyHandler(self)
        self.bullet_handler = BulletHandler()
        self.score = 0
        self.timer = 0
        self.number_deaths = 0
        self.best_score = 0

    def run(self):
        # Game loop: events - update - draw
        self.enemy_handler.clock = self.clock
        self.running = True
        while self.running:
            self.events()
            self.update()
            self.draw()
        pygame.display.quit()
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN and not self.playing:
                self.reset()
                self.playing = True

    def update(self):
        if self.playing:
            self.timer += self.clock.get_time() / 1000
            user_input = pygame.key.get_pressed()
            self.player.update(self.game_speed, user_input, self.bullet_handler)
            self.enemy_handler.update(self.bullet_handler)
            self.bullet_handler.update(self.player, self.enemy_handler.enemies)
            self.score = self.enemy_handler.enemies_destroyed
            if not self.player.is_alive:
                pygame.time.delay(300)
                self.playing = False
                self.number_deaths += 1
                if self.score > self.best_score:
                    self.best_score = self.score


    def draw(self):
        self.draw_background()
        if self.playing:
            self.clock.tick(FPS)
            self.player.draw(self.screen)
            self.enemy_handler.draw(self.screen)
            self.draw_timer(self.screen)
            self.bullet_handler.draw(self.screen)
            self.draw_score()
        else:
            self.draw_menu()
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed

    def draw_timer(self, screen):
        font = pygame.font.Font(None, 36)
        #como su nombre lo dice renderiza la fuente previamente creada y el 2f indica que despues de los dos puntos siguen 2 numeros de punto flotante, el true es para suavisar el renderizado
        text = font.render("Tiempo transcurrido: {:.2f}".format(self.timer), True, (255, 255, 255))
        screen.blit(text, (10, 10))

    def draw_menu(self):
        if self.number_deaths == 0:
            text, text_rect = text_utils.get_message('Press any key to start', 30, (255,255,255))
            self.screen.blit(text, text_rect)
        else:
            text, text_rect = text_utils.get_message('Press any key to restart', 30, (255,255,255))
            best_score, best_score_rect = text_utils.get_message(f'The best score is: {self.best_score}', 30, (255,255,255), heigth=SCREEN_HEIGHT//2 + 50)
            score, score_rect = text_utils.get_message(f'Your score is: {self.score}', 30, (255,255,255), heigth=SCREEN_HEIGHT//2 + 100)
            self.screen.blit(text, text_rect)
            self.screen.blit(best_score,best_score_rect)
            self.screen.blit(score, score_rect)
    
    def draw_score(self):
        score, score_rect = text_utils.get_message(f'Your score is: {self.score}', 20, (255,255,255), 1000, 40)
        self.screen.blit(score, score_rect)

    def reset(self):
        self.player.reset()
        self.enemy_handler.reset()
        self.bullet_handler.reset()
        self.score = 0
        self.timer = 0