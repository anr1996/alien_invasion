import pygame

class Rocket:
    """A  class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        
        
    # start each new ship at the bottom center of the screen.



        # load the ship image and get its rect.
        self.image = pygame.image.load('project(alien invasion)/images/rocket.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at  the bottom center of the screen.
        self.rect.center = self.screen_rect.center

        # Store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)

        # movement flag
        self.moving_right = False
        self.moving_left = False

    
    def update(self):
        """update the ship's position based on the movement flag."""
        # Update the ship's x value, not the rect.


        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.rocket_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.rocket_speed

        # Update rect object from self.x.
        self.rect.x = self.x


    def blitme(self):
        """Draw the rocket at its current location."""
        self.screen.blit(self.image, self.rect)
