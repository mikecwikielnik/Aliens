


import sys
from random import randint

import pygame

from settings13 import Settings 
from starr import Starr



class StarrInvasion:
    """Overall class to manage game assets and behavior. """
    
    def __init__(self):
        """Initialize the game, and create game resources. """
        pygame.init()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("STARR GRID")
        
        self.starr = pygame.sprite.Group()
        
        self._create_fleet()
        
    def run_game(self):
        """Start the main loop for the game. """
        while True:
            self._check_events()
            self._update_screen()
            
    def _check_events(self):
        "Respond to keypresses. "
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
                
    def _check_keydown_events(self, event):
        """Respond to q. """
        if event.key == pygame.K_q:
            sys.exit()
            
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.starr.draw(self.screen)
        
        pygame.display.flip()
        
    def _create_fleet(self):
        """Create a fleet of Starrs. """
        # Create a starr and find the number of starrs in a row.
        # Spacing between each starr is equal to one starr width
        starr = Starr(self)
        starr_width, starr_height = starr.rect.size
        available_space_x = self.settings.screen_width - (starr_width)
        number_starr_x = available_space_x // (2 * starr_width)
        
        # Determine the nummber of rows of starrs that fit on the screen.
        available_space_y = (self.settings.screen_height-
                             (2 * starr_height))
        number_rows = available_space_y // (2 * starr_height)
        
        # Create the full fleet of starrs
        for row_number in range(number_rows):
            for starr_number in range(number_starr_x):
                self._create_starr(starr_number, row_number)
                
    def _create_starr(self, starr_number, row_number): # watch your args here CAUTION!
        # Create a starr and place it in the row. 
        starr = Starr(self)
        starr_width, starr_height = starr.rect.size
        starr.x = starr_width + 2 * starr_width * starr_number
        starr.rect.x = starr.x
        starr.rect.y = starr_height + 2 * starr.rect.height * row_number
        
        
        starr.rect.x += randint(-5, 5)
        starr.rect.y += randint(-5, 5)
        self.starr.add(starr)
        
if __name__ == '__main__':
    # Make a game instance, and run the game
    st = StarrInvasion()
    st.run_game()
    
    
    