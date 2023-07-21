import pygame
import os

# Global Constants
TITLE = "Spaceships Game"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))

SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

POW = pygame.image.load(os.path.join(IMG_DIR, 'Other/pow.jpg'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = 'shield'

SPACESHIP = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))
SPACESHIP_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_shield.png"))
BULLET = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_1.png"))
BULLET_CHARGED = pygame.image.load(os.path.join(IMG_DIR, "Bullet/charge.png"))

BULLET_ENEMY = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_2.png"))
ENEMY_1 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_1.png"))
ENEMY_2 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_2.png"))
ENEMY_3 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_3.png"))
ENEMY_4 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_4.png"))

FONT_STYLE = 'freesansbold.ttf'

LEFT = 'left'
RIGTH = 'rigth'

BULLET_ENEMY_TYPE = 'enemy'
BULLET_PLAYER_TYPE = 'Spaceship'
CHARGED_BULLET_PLAYER_TYPE = 'charged'
BULLET_POW_TYPE = 'pow'

PLANET_1 = pygame.image.load(os.path.join(IMG_DIR, 'Other/planet_1.png'))
PLANET_2 = pygame.image.load(os.path.join(IMG_DIR, 'Other/planet_2.png'))