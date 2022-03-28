# 13-3. Raindrops: Find an image of a raindrop and create a grid of raindrops. Make the raindrops fall toward the bottom of the screen until they disappear.

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 268). No Starch Press. Kindle Edition. 

import sys
import pygame

from settings13 import Settings
from rain import Rain


class RainStorm:
    """Overall class to manage game assets and behavior. """
    
    def __init__(self):
        """Initialize the game, and create game resources. """
        pygame.init()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                               self.settings.screen_height))
        
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Rain Storm")
        
        self.rain = pygame.sprite.Group()
        
        self._create_storm()
        
    def run_game(self):
        """Start the main loop for the game. """
        while True:
            self._check_events()
            self._update_rain()
            self._update_screen()
            
    def _check_events(self):
        """Respond to keypresses. """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
    
    def _check_keydown_events(self, event):
        """Respond to q. """
        if event.key == pygame.K_q:
            sys.exit()
                  
    def _create_storm(self):
        """Create a rainstorm. """
        # Crate rain and find the number of raindrops in a row. 
        # Spacing between each drop is equal to one drop width
        rain = Rain(self)
        rain_width, rain_height = rain.rect.size
        available_space_x = self.settings.screen_width - rain_width
        
        # We'll need this number again to make new rows. 
        self.number_rain_x = available_space_x // (2 * rain_width)
        
        # Determine the number of rows of rain that fit on the screen.
        available_space_y = self.settings.screen_height
        number_rows = available_space_y // (2 * rain_height)
        
        # Fill the sky with drops.
        for row_number in range(number_rows):
            self._create_row(row_number)
    
    def _create_row(self, row_number):   
        # Create the full storm
        for rain_number in range(self.number_rain_x):
            self._create_rain(rain_number, row_number)
                
    def _create_rain(self, rain_number, row_number): # watch your args here CAUTION!
        # Create a drop and place it in the row 
        rain = Rain(self)
        rain_width, rain_height = rain.rect.size
        rain.rect.x = rain_width + 2 * rain_width * rain_number
        rain.y = 2 * rain.rect.height * row_number
        rain.rect.y = rain.y
        self.rain.add(rain)

    def _update_rain(self):
        """
        Check if the fleet is at an edge, 
            then update the position of all aliens in the fleet. 
        """
        self.rain.update()
        
        # Assume we won't make new drops
        make_new_drops = False
        for drop in self.rain.copy():
            if drop.check_disappeared():
                # Remove this drop, and we'll need to make new drops
                self.rain.remove(drop)
                make_new_drops = True
        
        # Make a new row of rain if needed
        if make_new_drops:
            self._create_row(0)
        
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.rain.draw(self.screen)
        
        pygame.display.flip()
        
if __name__ == '__main__':
    # Make a game instance, and run the game 
    rs = RainStorm()
    rs.run_game()
    
    