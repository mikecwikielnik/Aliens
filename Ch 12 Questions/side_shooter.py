from hashlib import sha1
import sys 
import pygame

from side_settings import Side_Setting
from side_ship import Side_Ship
# from side_bullet import Side_Bullet

class Side_Shooter:
    """Overall class to manage game assets and behavior. """
    
    def __init__(self):
        """Initiliaze the game, and create game resources. """
        pygame.init()
        self.side_settings = Side_Setting()
        
        # To get a small screen, remove the pygame.FULLSCREEN
        self.screen = pygame.display.set_mode((500, 500)) # pygame.FULLSCREEN)
        
        self.side_settings.screen_height = self.screen.get_rect().height
        self.side_settings.screen_width = self.screen.get_rect().width
        pygame.display.set_caption("Side Shooter game")
        
        self.side_ship = Side_Ship(self)
        # self.bullets = pygame.sprite.Group()
        
    def run_game(self):
        """Start the main loop for the game. """
        while True:
            self._check_events()
            self.side_ship.update()
            # self._update_bullets()
            self._update_screen()
            
    def _check_events(self):
        """Respond to keypresses and mouse events. """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keydown_events(event)
    
    def _check_keydown_events(self, event):
        """Respond to keypresses. """
        if event.key == pygame.K_UP:
            self.side_ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.side_ship.moving_down = True
        elif event.key == pygame.K_q:
            sys.quit()
        
    def _check_keyup_events(self, event):
        """Respond to key releases. """
        if event.key == pygame.K_UP:
            self.side_ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.side_ship.moving_down = False
            
            # Make the most recently drawn screen visible
            pygame.display.flip()
        
    # def _fire_bullet(self):
        
    # def _update_bullets(self):
        
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen. """
        self.screen.fill(self.side_settings.bg_color)
        self.side_ship.blitme()
        
        pygame.display.flip()
        
if __name__ == '__main__':
    # Make a game instance, and run the game.
    ss_game = Side_Shooter()
    ss_game.run_game()
    
