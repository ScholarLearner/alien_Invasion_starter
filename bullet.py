"""
This is the bullet file
F.Martin
This is the bullet function
10/30/2026
"""
import pygame 
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Bullet(Sprite):
    def __init__(self, game: 'AlienInvasion'):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings

        self.bg = pygame.image.load(self.settings.bullet_file)
        self.bg =pygame.transform.scale(self.bg,
            (self.settings.bullet_w,self.settings.bullet_h)
 )
        self.rect = self.bg.get_rect()
        self.rect.midtop = game.ship.rect.midtop
        self.y = float(self.rect.y)

    def update(self):

        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        self.screen.blit(self.bg, self.rect)