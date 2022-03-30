import pygame


class Redfield:
    """A class to manage Chris Redfield. """
    
    def __init__(self, qt_game):
        """Initialize Chris and set its starting position. """
        self.screen = qt_game.screen
        self.settings = qt_game.settings
        self.screen_rect = qt_game.screen.get_rect()
        
            # Load the chris image and get is rect 
        self.image = pygame.image.load('redfield.bmp')
        self.rect = self.image.get_rect()
            # Start each new chris at the center of the screen
        self.rect.center = self.screen_rect.center
            # Store a decimal value for the ship's horizontal position
            # and vertical position. 
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
            # Movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        
    def update(self):
        """Update the ship's position based on the movemment flag. """
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.redfield_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.redfield_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.redfield_speed
        if self.moving_down and self.rect.bottom <= self.screen_rect.bottom:
            self.y += self.settings.redfield_speed
        
            
            # Update the rect object from self.x
        self.rect.x = self.x 
        self.rect.y = self.y 
        
    def blitme(self):
        """Draw chris at its current location. """
        self.screen.blit(self.image, self.rect)
        
