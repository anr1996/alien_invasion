import sys
from random import random

import pygame
from time import sleep

from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien
from scoreboard import Scoreboard
from button import Button
from alien_bomb import Alien_bomb

class SidewaysShooter:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
                (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Sideways Shooter")


        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.bombs = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()


    # Make the Play button.
        self.Play_button = Button(self, "Play")
        
        self._create_alien()


        """Setting the Background Color"""
        self.bg_color = (250,235,215)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            if self.stats.game_active:

                 # Consider creating a new alien.
    
                self.ship.update()
                self._update_bullets()
                self.aliens.update()
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)  



    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play."""
        button_clicked = self.Play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self.reset_statistics()


    def reset_statistics(self):
        # Reset the game statistics.
        self.settings.initialize_dynamic_settings()
        self.stats.reset_stats()
        self.stats.game_active = True 
        self.sb.prep_score()
        self.sb.prep_level()
        self.sb.prep_ships()
            
        self.aliens.empty()
        self.bullets.empty()
        self.bombs.empty()

        # create a new fleet and center the ship.
        self._create_alien()
        self.ship.center_ship()

        # hide the mouse coursor.
        pygame.mouse.set_visible(False)  

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)


    def _fire_alien_bomb(self): 
        """drop bombs from alien ships"""
        for alien in self.aliens:
            if len(self.bombs) < self.settings.bombs_allowed:
                new_bomb = Alien_bomb(self, alien.x, alien.y)
                self.bombs.add(new_bomb)

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet positions.
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
                    # printing len of bullets just verifies that the bullets are being removed once off the game screen.
        print(len(self.bullets)) 
        self._check_bullet_alien_collisions()



    def _fire_alien_bomb(self): 
        """drop bombs from alien ships"""
        for alien in self.aliens:
            if len(self.bombs) < self.settings.bombs_allowed:
                new_bomb = Alien_bomb(self, alien.x, alien.y)
                self.bombs.add(new_bomb)


        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.screen.get_rect().right:
                 self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Check whether any bullets have hit an alien."""
        collisions = pygame.sprite.groupcollide(
                self.bullets, self.aliens, True, True)

        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()


        if not self.aliens:
            # Destroy existing bullets and create new fleet.
            self.bullets.empty()
            self.bombs.empty()
            self._create_alien()
            self.settings.increase_speed()

            # Increase level.
            self.stats.level += 1
            self.sb.prep_level()

    def _ship_hit(self):
        """Respond to the ship being hit by an alien."""
        if self.stats.ships_left > 0:
            # Decrement ships_left, and update scoreboard.
            self.stats.ships_left -= 1
            self.sb.prep_ships()

            # get rid of any remaining aliens and bullets.
            self.aliens.empty()
            self.bullets.empty()
            self.bombs.empty() 

            # Create a new fleet and center the ship.
            self._create_alien()
            self.ship.center_ship()
        
        # Pause.
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

        

    def _create_alien(self):
        """Create an alien, if conditions are right."""
        if random() < self.settings.alien_frequency:
            alien = Alien(self)
            self.aliens.add(alien)
            print(len(self.aliens))

    
    def _check_aliens_left_screen(self):
        """Check if any aliens have reached the left of the screen."""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.left >= screen_rect.left:
                # Treat this the same as if the ship got hit.
                self._ship_hit()
                break


    def _update_aliens(self):
       
        """update the positions of all aliens in the fleet."""
        self.aliens.update()

        # Look for alien-ship collisions.
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        
        # look for any bomb-ship collisions.
        if pygame.sprite.spritecollideany(self.ship, self.bombs):
            self._ship_hit()

            # Look for aliens hitting the bottom of the screen.
        self._check_aliens_left_screen()
      

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.aliens.draw(self.screen)

        for bomb in self.bombs.sprites():
                bomb.draw_bomb()

        # Draw the score information.
        self.sb.show_score()

        # Draw the play button if the game is inactive.
        if not self.stats.game_active:
            self.Play_button.draw_button()

        pygame.display.flip()



if __name__ == '__main__':
    # Make a game instance, and run the game.
    ss_game = SidewaysShooter()
    ss_game.run_game()
