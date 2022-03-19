# 12-2. Game Character: Find a bitmap image of a game character you like or convert an image to a bitmap. 

# Make a class that draws the character at the center of the screen and match the background color of the image to the background color of the screen, or vice versa.

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 238). No Starch Press. Kindle Edition. 

import sys 
import pygame

from settings import Settings
from redfield import Redfield

class BlueWindow:   
    """Create a blue pygame window. """
    
    def __init__(self):
        """Initialize the class. """
        pygame.init()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Question 12-2")
        
        self.redfield = Redfield(self)
        
    def run_question(self):
        """Start the main loop for the game. """
        while True:
            self._check_events()
            self._update_screen()
            
    def _check_events(self):
        """Respond to keypresses and mouse events. """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
            # Make the most recently drawn screen visible. 
            pygame.display.flip()
                    
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen. """
        self.screen.fill(self.settings.bg_color)
        self.redfield.blitme()
        
        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game. 
    qt = BlueWindow()
    qt.run_question()