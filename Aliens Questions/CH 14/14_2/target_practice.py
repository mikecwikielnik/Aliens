import sys
from random import random

import pygame

from settings import Settings
from game_stats import GameStats
from button import Button
from ship import Ship
from bullet import Bullet
from target import Target

class TargetPractice:
    """Overall class to manage game assets and behavior. """
    
    def __init__(self): 
        """Initialize the game, and create game resources. """
        pygame.init()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Target Practice")
        
        # Create an instance to store game statistics.
        self.stats = GameStats(self)
        
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.target = Target(self)
        
        # Make the Play button.
        self.play_button = Button(self, "Play")
        
    def run_game(self):
        """Start the main loop for the game. """
        while True:
        