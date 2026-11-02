"""Settings File
F.Martin
Making class function of settings
10/18/2026"""

from pathlib import Path 

class Settings:

    def __init__(self):
        """ Settings for screen """
        self.name: str = 'Alien Invasion'
        self.screen_w = 1200
        self.screen_h = 800 
        self.FPS = 60
        self.bg_file = Path.cwd() / 'Assets' / 'images' / 'Starbasesnow.png'
        self.ship_file = Path.cwd() /'Assets'/'images'/ 'durrrSpaceShip.png'
        self.ship_w = 40
        self.ship_h = 60
        self.ship_speed = 5