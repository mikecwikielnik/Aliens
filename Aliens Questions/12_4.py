# 12-4. 

# Allow the player to move up, down, left, or right using the four arrow keys. 

# Make sure the player never moves beyond any edge of the screen.

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 246). No Starch Press. Kindle Edition. 



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
        
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Question 12-4")
        
        self.redfield = Redfield(self)
        
    def run_question(self):
        """Start the main loop for the game. """
        while True:
            self._check_events()
            self.redfield.update()
            self._update_screen()
            
    def _check_events(self):
        """Respond to keypresses and mouse events. """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

                
    def _check_keydown_events(self, event):
        """Respond to keypresses. """
        if event.key == pygame.K_RIGHT:
            self.redfield.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.redfield.moving_left = True
        if event.key == pygame.K_UP:
            self.redfield.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.redfield.moving_down = True
        elif event.key == pygame.K_q:
            sys.quit()
            
    def _check_keyup_events(self, event):
        """Respond to key releases. """
        if event.key == pygame.K_RIGHT:
            self.redfield.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.redfield.moving_left = False
        if event.key == pygame.K_UP:
            self.redfield.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.redfield.moving_down = False
        elif event.key == pygame.K_q:
            sys.quit()
            
            
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