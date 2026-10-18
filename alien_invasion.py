"""Alien Invasion
F.Martin
Operating om Alien Invasion
10/17/2026 """


import sys
import pygame
from settings import Settings

class AlienInvasion:

    def __init__(self) -> None:
        pygame.init()
        self.settings = Settings()

        self.screen =pygame.display.set_mode((self.settings.screen_w,self.settings.screen_h))
        pygame.display.set_caption(self.settings.name)

        self.running = True
        self.clock = pygame.time.Clock()

    def run_game(self):
    #    The Game loop
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.flip()
            self.clock.tick(self.settings.FPS)




if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()