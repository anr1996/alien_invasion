
import sys
from settings import Settings
import pygame

class Keys:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Screen test")

        

        """Setting the Background Color"""
        self.bg_color = (255, 255, 255)

    def run_game(self):
        """Start the main loop for the game."""

        while True:
            self._check_events()
            self._update_screen()


    def _check_events(self):
        """respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    
    def _check_keydown_events(self, event):
        """respond to keypresses"""
        if event.key == pygame.K_RIGHT:
            pygame.display.set_caption("hello there!")
        elif event.key == pygame.K_LEFT:
            pygame.display.set_caption("good bye!")
        elif event.key == pygame.K_q:
            sys.exit()



    def _check_keyup_events(self, event):
        """Respond to key releases"""
        if event.key == pygame.K_RIGHT:
            print("")
        elif event.key == pygame.K_LEFT:
            print("")




                 
                    



    def _update_screen(self):
        """update images on the screen, and flip to the new screen"""

        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        
        # Make the most recent drawn screen visible.
        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance and run the game.
    ai = Keys()
    ai.run_game()


