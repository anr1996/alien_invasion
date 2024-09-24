import sys

import pygame

from settings import Settings
from raindrop import Raindrop
from ship import Ship
from bullet import Bullet

class RaindropsGame:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
                (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Raindrops")


        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.raindrops = pygame.sprite.Group()
        self._create_fleet()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_raindrops()
            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        if event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()


    def _check_keyup_events(self, event):
        """Respond to key releases"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)  


    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
                    # printing len of bullets just verifies that the bullets are being removed once off the game screen.
        print(len(self.bullets)) 


    """ def _create_drops(self):
        """"Fill the sky with raindrops.""""
        # Create an drop and find the number of drops in a row.
        # Spacing between each drop is equal to one drop width.
        #   Note that the spacing here works reasonably for larger drops.
        #   If you're working with smaller drops, there might be a better
        #   approach to spacing.
        drop = Raindrop(self)
        drop_width, drop_height = drop.rect.size
        available_space_x = self.settings.screen_width - drop_width

        # We'll need this number again to make new rows.
        self.number_drops_x = available_space_x // (2 * drop_width)
        
        # Determine the number of rows of drops that fit on the screen.
        available_space_y = self.settings.screen_height
        number_rows = available_space_y // (2 * drop_height)
        
        # Fill the sky with drops.
        for row_number in range(number_rows):
            self._create_row(row_number)

    def _create_row(self, row_number):
        """"Create a single row of raindrops.""""
        for drop_number in range(self.number_drops_x):
            self._create_drop(drop_number, row_number)

    def _create_drop(self, drop_number, row_number):
        """"Create an drop and place it in the row.""""
        drop = Raindrop(self)
        drop_width, drop_height = drop.rect.size
        drop.rect.x = drop_width + 2 * drop_width * drop_number
        drop.y = 2 * drop.rect.height * row_number
        drop.rect.y = drop.y
        self.raindrops.add(drop)
 """




    def _create_fleet(self):
        """Create the fleet of aliens."""
        # Make an alien.
        raindrop = Raindrop(self)
        raindrop_width, raindrop_height = raindrop.rect.size
        available_space_x = self.settings.screen_width - (2 * raindrop_width)
        number_raindrop_x = available_space_x // (2 * raindrop_width)
        
        
        #Determine the number of rows of aliens that fit on the screen.
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - 
        (3 * raindrop_height) - ship_height)
        number_rows = available_space_y // (2 * raindrop_height)
        


        # Create the full row of aliens.
        for row_number in range(number_rows):
            for raindrop_number in range(number_raindrop_x):
                self._create_raindrop(raindrop_number, row_number) 
            


    def _create_raindrop(self, raindrop__number, row_number):
        raindrop = Raindrop(self)
        raindrop_width, raindrop_height = raindrop.rect.size
        raindrop.x = raindrop_width + 2 * raindrop_width * raindrop__number 
        raindrop.rect.x = raindrop.x
        raindrop.rect.y = raindrop_height + 2 * raindrop.rect.height * row_number
        self.raindrops.add(raindrop)


    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for raindrop in self.raindrops.sprites():
            if raindrop.check_edges():
                self._change_fleet_direction()
                break

    
    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for raindrop in self.raindrops.sprites():
            raindrop.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1


    
    def _update_raindrops(self):
        
        
        self.raindrops.update()
        
        # Assume we won't make new drops.
        make_new_drops = False
        for drop in self.raindrops.copy():
            if drop.check_disappeared():
                # Remove this drop, and we'll need to make new drops.
                self.raindrops.remove(drop)
                make_new_drops = True

        # Make a new row of drops if needed.
        if make_new_drops:
            self._create_row(0)  



    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet() 
        self.raindrops.draw(self.screen)

        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    rd_game = RaindropsGame()
    rd_game.run_game()
