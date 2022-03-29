import pygame

from pygame.sprite import Sprite

class Side_Alien(Sprite):
    """A class to represent a single alien in the fleet. """
    
    def __init__(self, ai_game):
        """Initialize the alien and set its starting position. """
        super().__init__()
        self.screen = ai_game.screen
        self.screen = ai_game.side_settings
        
        # Load the alien image and set its rect attribute
        
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        
        # Start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        # Store the alien's exact horizontal position
        self.x = float(self.rect.x)
        
    def check_edges(self):
        """Return True if alien is at edge of screen. """
        screen_rect = self.screen.get_rect()
        if self.rect.top or self.rect.bottom <= 0:
            return True
        
    def update(self):
        """Move the alien up or down. """
        self.y += (self.side_settings.alien_speed * 
                   self.side_settings.fleet_direction)
        self.rect.y = self.y