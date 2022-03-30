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
        
        self.y = float(self.rect.y)
        
    def check_disappeared(self):
        """Check if drop has disappeared off bottom of screen. """
        if self.rect.top > self.screen.get_rect().bottom:
            return True
        else: 
            return False
        
    def update(self):
        """Move the alien to the right or left. """
        self.y += self.settings.rain_speed
        self.rect.y = self.y 