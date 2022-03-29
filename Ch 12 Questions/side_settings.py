
class Side_Setting:
    """A class to store all settings for question 12-6. """
    
    def __init__(self):
        """Initialize the game's settings. """
        self.screen_width = 500
        self.screen_height = 500
        self.bg_color = (255, 255, 255)
        # Ship settings
        self.side_ship_speed = 1.5
        
        # # Bullet Settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed= 3
        
        # Alien Settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
        
        