import pygame 

from pygame.sprite import Sprite

class Starr(Sprite):
    """A class to represent a single alien in the fleet. """
    
    def __init__(self, st_game):
        """Initialize the starrr and set its starting position. """
        super().__init__
        self.screen = st_game.screen
        
        # Load the starr image and set its rect attribute
        self.image = pygame.image.load('starr.bmp')
        self.rect = self.image.get_rect()
        
        # Start each new starr near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        # Store the starr's exact horizontal position
        self.x = float(self.rect.x)
        
        
        