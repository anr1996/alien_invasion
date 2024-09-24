class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):

        # Alien settings
        self.alien_speed = 5.0
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
        




        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (100,100,100)

       

       # Ship settings
        self.ship_speed = 100.5 # 3.5 is the default setting
        self.ship_limit = 3

        # bullet settings
        self.bullet_speed = 300.0 # 7.0 is  the default setting
        self.bullet_width = 10 # default setting is 3 
        self.bullet_height = 15
        self.bullet_color = (60,  60, 60)
        self.bullets_allowed = 1000 # 3 is the default setting

        self.bomb_speed = 1
        self.bomb_width = 10
        self.bomb_height = 10
        self.bomb_color = (50, 40, 20)
        self.bombs_allowed = 10

        # How quickly the game speeds up
        self.speedup_scale = 1.3 # 1.1 is the default setting

        # How quickly the alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 4.5 # 1.5 is the default setting
        self.bullet_speed = 1.0 # 3.0 is the default setting
        self.alien_speed = 0.3 # 1.0 is the default setting
        self.bomb_speed = 0.2

        # Scoring
        self.alien_points = 50
    
    # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

    def increase_speed(self):
        """increase speed settings and alien point values."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.bomb_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)   

    