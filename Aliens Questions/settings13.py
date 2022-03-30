
class Settings:
    """A class to store settings for Star Invasion. """
    
    def __init__(self):
        """Initialize the game's setting. """
        # Screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (255, 255, 255)
        
        
        # Rain Settings
        self.rain_speed = 1.0
        self.storm_drop_speed = 10
        # storm_direction of 1 represents right; -1 represents left. 
        self.storm_direction = 1 
        