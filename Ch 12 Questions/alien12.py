from pkgutil import ImpImporter
import pygame

from random import randint
from pygame.sprite import Sprite

class Side_Alien(Sprite):
    """A class to represent a single alien in the fleet. """
    
    def __init__(self, ss_game):
        """Initialize the alien and set its starting position. """
        super().__init__()
        self.screen = ss_game.screen
        self.settings = ss_game.side_settings
        
        # Load the alien image and set its rect attribute
        
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        
        # Start each new alien at a random positioni on the right side
        #   of the screen.
        self.rect.left = self.screen.get_rect().right
        # The farthest down the screen we'll place the alien is the height
        #   of the screen, minus the height of the alien.
        alien_top_max = self.settings.screen_height - self.rect.height
        self.rect.top = randint(0, alien_top_max)

        # Store the alien's exact horizontal position
        self.x = float(self.rect.x)
        
    def update(self):
        """Move the alien up or down. """
        self.x -= self.settings.alien_speed
        self.rect.x = self.x