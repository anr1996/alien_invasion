import pygame
from pygame.sprite import Sprite
 
class Raindrop(Sprite):
    """A class to represent a single raindrop."""

    def __init__(self, rd_game):
        """Initialize the raindrop and set its starting position."""
        super().__init__()
        self.screen = rd_game.screen
        self.settings = rd_game.settings

        # Load the raindrop image and set its rect attribute.
        #   Raindrop image from: https://commons.wikimedia.org/wiki/File:Antu_raindrop.svg
        #   License: https://creativecommons.org/licenses/by-sa/3.0/deed.en
        #   Modified size, and cropped.
        self.image = pygame.image.load('Try It Yourself (pg268)/my_raindrop.bmp')
        self.rect = self.image.get_rect()

        # Start each new raindrop near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the raindrop's exact horizontal position.
        self.x = float(self.rect.x)


    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()

        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True



    def check_disappeared(self):
        """Check if drop has disappeared off bottom of screen."""
        if self.rect.top > self.screen.get_rect().bottom:
            return True
        else:
            return False




    def update(self):
        """Move the alien to the right."""
        self.x += (self.settings.raindrop_speed *
            self.settings.fleet_direction)
        self.rect.x = self.x 



    """ def update(self):
        """"Move the raindrop down the screen.""""
        self.y += self.settings.raindrop_speed
        self.rect.y = self.y
 """