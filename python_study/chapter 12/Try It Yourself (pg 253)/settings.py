class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):



        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (250,235,215)

       

       # Ship settings
        self.ship_speed = 3.5

        # bullet settings
        self.bullet_speed = 7.0
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (60,  60, 60)
        self.bullets_allowed = 3


# Alien settings.
        #  alien_frequency controls how often a new alien appear.s
        #    Higher values -> more frequent aliens. Max = 1.0.
        self.alien_frequency = 0.008
        self.alien_speed = 2.5