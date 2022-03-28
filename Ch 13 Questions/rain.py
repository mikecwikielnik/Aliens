import pygame

from pygame.sprite import Sprite

class Rain(Sprite):
    """A class to represent a single raindrop in the storm. """
    
    def __init__(self, rain_game):
        """Initialize the rain and set its starting position. """
        super().__init__()
        self.screen = rain_game.screen
        self.settings = rain_game.settings
        
        # Load the rain image and set its rect attributes
        
        self.image = pygame.image.load('rain.bmp')
        self.rect = self.image.get_rect()
        
        # Start each new alien near the top left of the screen.
        
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height 
        
        # Store the alien's exact horizontal position. 
        
        self.x = float(self.rect.x)
        
    def check_edges(self):
        """Return True if alien is at edge of screen. """
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True 
        
    def update(self):
        """Move the alien to the right or left. """
        self.x += (self.settings.rain_speed *
                   self.settings.storm_direction)
        self.rect.x = self.x 