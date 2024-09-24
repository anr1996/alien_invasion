import pygame
from pygame.sprite import Sprite


class Alien_bomb(Sprite):
    """A  class to manage bullets fired from the ship"""


    def __init__(self, ai_game, x, y):
        """Create a bullet object at  the ship's current position."""
        super().__init__()
        self.screen = ai_game.screen 
        self.settings = ai_game.settings 
        self.color = self.settings.bomb_color
        

        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(x, y, self.settings.bomb_width,
            self.settings.bomb_height)

        self.y = y


        """ self.rect.midbottom = ai_game.alien.rect.midbottom  """

        """   # Store the bullet's position as a decimal value.
            self.y = float(self.rect.y) """

    def update(self):
        """Move the bullet up the screen."""
        # Update the decimal position of the bullet.
        self.y += self.settings.bomb_speed
        
        # Update the rect position.
        self.rect.y = self.y

    def draw_bomb(self):
        """Draw the bullet to the screen."""

        pygame.draw.rect(self.screen, self.color, self.rect)