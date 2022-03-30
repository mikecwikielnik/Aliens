# 12-1. Blue Sky: Make a Pygame window with a blue background.

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 238). No Starch Press. Kindle Edition. 


import sys 
import pygame

class BlueWindow:
    """Create a blue pygame window. """
    
    def __init__(self):
        """Initialize the class. """
        pygame.init()
        self.screen = pygame.display.set_mode((500,500))
        self.bg_color = (0,0,255)
        pygame.display.set_caption("Question 12-1")
        
    def run_question(self):
        """Start the main loop for the game. """
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    
    def _update_screen(self):
            self.screen.fill(self.bg_color)
            pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game. 
    qt = BlueWindow()
    qt.run_question()