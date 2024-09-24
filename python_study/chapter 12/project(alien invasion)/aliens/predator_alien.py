import pygame

class Alien_predator:

    """alien predator type character"""

    def __init__(self, ai_game):
        """Initialize the character and set its position"""

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # load the alien image and get its rect.

        self.image = pygame.image.load('project(alien invasion)/images/red_alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the middle center of the screen.
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Draw the alien at its current location."""
        self.screen.blit(self.image, self.rect)



