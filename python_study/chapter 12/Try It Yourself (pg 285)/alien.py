import pygame
from pygame.sprite import Sprite



class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings 
        self.screen_rect = ai_game.screen.get_rect()

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('project(alien invasion)/predator.bmp')
        self.rect = self.image.get_rect()

            
        
        self.rect.midbottom = self.screen_rect.midbottom

     

        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)

    """  # Start each new alien near the top left of the screen.
        self.rect.midright = self.rect.width
        self.rect.midright = self.rect.height  """