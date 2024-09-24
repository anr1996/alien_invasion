import pygame

class Ship:
    """A  class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        
        
    # start each new ship at the bottom center of the screen.



        # load the ship image and get its rect.
        self.image = pygame.image.load('project(alien invasion)/images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at  the bottom center of the screen.
        self.rect.midleft = self.screen_rect.midleft

        # Store a decimal value for the ship's horizontal position.
        self.y = float(self.rect.y)

        # movement flag
        self.moving_up = False
        self.moving_down = False




    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.midleft = self.screen_rect.midleft
        self.y = float(self.rect.y)

    
    def update(self):
        """update the ship's position based on the movement flag."""
        # Update the ship's x value, not the rect.


        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed

        # Update rect object from self.x.
        self.rect.y = self.y


    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)