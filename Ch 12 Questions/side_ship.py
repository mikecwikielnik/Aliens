import pygame


class Side_Ship:
    """A class to manage the ship in question 12-6. """
    
    def __init__(self, ss_game):
        """Initialize Side Ship and set its starting position. """
        self.screen = ss_game.screen
        self.side_settings = ss_game.side_settings
        self.screen_rect = ss_game.screen.get_rect()
        
        # Load the ship image and get its rect
        self.image = pygame.image.load('ship.bmp')
        self.rect = self.image.get_rect()
        
        # Start each new ship at the center 
        self.rect.midleft = self.screen_rect.midleft
        
        # Store a decimal value for ships vertical position
        self.y = float(self.rect.y)
        
        # Movement flags
        self.moving_up = False
        self.moving_down = False 
        
    def update(self):
        """Update the ship's position based on the movement flag. """
        if self.moving_up and self.rect.top > 0:
            self.y -= self.side_settings.side_ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.side_settings.side_ship_speed
        
        # Update the rect object from self
        self.rect.y = self.y
        
    def blitme(self):
        """Draw Chris at its current location. """
        self.screen.blit(self.image, self.rect)
        
