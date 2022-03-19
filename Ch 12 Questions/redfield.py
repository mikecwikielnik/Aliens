import pygame

class Redfield:
    """A class to manage Chris Redfield. """
    
    def __init__(self, qt_game):
        """Initialize Chris and set its starting position. """
        self.screen = qt_game.screen
        self.screen_rect = qt_game.screen.get_rect()
        
        # Load the chris image and get is rect 
        self.image = pygame.image.load('redfield.bmp')
        self.rect = self.image.get_rect()
        # Start each new chris at the center of the screen
        self.rect.center = self.screen_rect.center
        
    def blitme(self):
        """Draw chris at its current location. """
        self.screen.blit(self.image, self.rect)
        
