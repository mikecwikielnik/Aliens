
class Side_Setting:
    """A class to store all settings for question 12-6. """
    
    def __init__(self):
        """Initialize the game's settings. """
        self.screen_width = 500
        self.screen_height = 500
        self.bg_color = (255, 255, 255)
        # Ship settings
        self.side_ship_speed = 3.0
        
        # # Bullet Settings
        self.bullet_speed = 1.0
        self.bullet_width = 40
        self.bullet_height = 3
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        
        # Alien Settings
        # alien_frequency controls how often a new alien appear's
        #   Higher values -> more frequent aliens. Max = 1.0
        self.alien_frequency = 0.008
        self.alien_speed = 0.5
        