
import sys 

from random import random

import pygame

from side_settings import Side_Setting
from game_stats import GameStats
from side_ship import Side_Ship
from side_bullet import Side_Bullet 
from alien12 import Side_Alien

class Side_Shooter:
    """Overall class to manage game assets and behavior. """
    
    def __init__(self):
        """Initiliaze the game, and create game resources. """
        pygame.init()
        self.side_settings = Side_Setting()
        
        # To get a small screen, remove the pygame.FULLSCREEN
        self.screen = pygame.display.set_mode(
            (self.side_settings.screen_width, self.side_settings.screen_height))
        pygame.display.set_caption("Side Shooter game")
        
        # Create an instance to store game stats
        self.stats = GameStats(self)
        
        self.side_ship = Side_Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
    
        
    def run_game(self):
        """Start the main loop for the game. """
        while True:
            self._check_events()

            if self.stats.game_active:
                self._create_alien()
                
                self.side_ship.update()
                self._update_bullets()
                self._update_alien()
                
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
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()

        
    def _check_keyup_events(self, event):
        """Respond to key releases. """
        if event.key == pygame.K_UP:
            self.side_ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.side_ship.moving_down = False
            
    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group. """
        if len(self.bullets) < self.side_settings.bullets_allowed:
            new_bullet = Side_Bullet(self)
            self.bullets.add(new_bullet)
        
    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets. """
        # Update bullet positions.
        self.bullets.update()
        
        # Get rid of bullets that have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.screen.get_rect().right:
                self.bullets.remove(bullet)
                
        self._check_bullet_alien_collisions()
        
    def _check_bullet_alien_collisions(self):
        """Respond to bullet-alien collisions. """
        # Remove any bullets and aliens that have collided.
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)
        
        if not self.aliens:
            # Destroy existing bullets and create new fleet
            self.bullets.empty()
            self._create_alien()
                
    def _create_alien(self):
        """Create an alien, if conditions are right.  """
        if random() < self.side_settings.alien_frequency:
            alien = Side_Alien(self)
            self.aliens.add(alien)
            print(len(self.aliens))
            
    def _update_alien(self):
        """Update alien positions, and look for collisions with ship. """
        self.aliens.update()
        
        if pygame.sprite.spritecollideany(self.side_ship, self.aliens):
            self._ship_hit()
        
        # Look for aliens that have hit the left edge of the screen.
        self._check_aliens_left_edge()
        
    def _check_aliens_left_edge(self):
        """
        Respond to aliens that have hit left edge of the screen. 
            Treat this the same as the ship getting hit. 
        """
        
        for alien in self.aliens.sprites():
            if alien.rect.left < 0:
                self._ship_hit
                break
            
    def _ship_hit(self):
        """Respond to the ship being hit by an alien. """
        if self.stats.ships_left > 0:
            # Decrement ships_left
            self.stats.ships_left -= 1
            
            # Get rid of any remaining aliens and bullets
            self.aliens.empty()
            self.bullets.empty()
            
            # Center the ship
            self.side_ship.center_ship()
        else:
            self.stats.game_active = False

    
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen. """
        self.screen.fill(self.side_settings.bg_color)
        self.side_ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
            
        self.aliens.draw(self.screen)
        
        pygame.display.flip()


        
if __name__ == '__main__':
    # Make a game instance, and run the game.
    ss_game = Side_Shooter()
    ss_game.run_game()
    
    
    
    

    
      # def _create_fleet(self):
    #     """Create the fleet of aliens. """
    #     # Create an alien and find the number of aliens in a row.
    #     # Spacing between each alien is equal to one alien width
    #     alien = Side_Alien(self)
    #     alien_width, alien_height = alien.rect.size
    #     available_space_x = self.side_settings.screen_width - alien_width
    #     number_alien_x = available_space_x // (2 * alien_width)
        
    #     # Determine the number of rows of aliens that fit on the screen.
    #     ship_height = self.side_ship.rect.height
    #     available_space_y = (self.side_settings.screen_height - 
    #                          (3 * alien_height)- ship_height)
    #     number_rows = available_space_y // (2 * alien_height)
        
    #     # Create the full fleet of aliens
    #     for row_number in range(number_rows):
    #         for alien_number in range(number_alien_x):
    #             self._create_alien(alien_number, row_number)
    
        # def _check_fleet_edges(self):
    #     """Respond appropriately if any aliens have reached an edge. """
    #     for alien in self.aliens.sprites():
    #         if alien.check_edges():
    #             self._change_fleet_direction()
    #         break
    
    # def _change_fleet_direction(self):
    #     """Drop the entire fleet and change the fleet's direction. """
    #     for alien in self.aliens.sprites():
    #         alien.rect.y += self.side_settings.fleet_drop_speed
    #     self.side_settings.fleet_direction *= -1