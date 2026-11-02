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
        """ Settings for bullets """
        self.bullet_file = Path.cwd() / 'Assets' / 'images' / 'laserBlast.png'
        self.laser_sound = Path.cwd() / 'Assets' / 'sounds' / 'laser.mp3'
        self.bullet_speed= 7
        self.bullet_w = 25
        self.bullet_h = 80
        self.bullet_amount = 5
