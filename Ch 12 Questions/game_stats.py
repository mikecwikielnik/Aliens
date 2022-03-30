
class GameStats:
    """Track statistics for Sider Shooter. """
    
    def __init__(self, ss_game):
        """Initialize stats. """
        self.side_settings = ss_game.side_settings
        self.reset_stats()
        
        # Start side shooter in an active state. 
        self.game_active = True
        
    def reset_stats(self):
        """Initialize statistics that can change during the game. """
        self.ships_left = self.side_settings.ship_limit