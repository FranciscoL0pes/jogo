import sys
import pygame
from settings import Settings 
from ship import Ship





class AlienInvasion:
    """Classe pricipal para gerir os recusos e comportamentos do jogo Alien Invasion. """

    def __init__(self):
        """iniciazliza e cria os recursos do jogo."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion by Francisco Lopes")
        self.ship = Ship(self)
        self.bg_color = (self.settings.bg_color)
        
        
        
       

    def run_game(self):
        """iniciazila o loop principal do jogo. """
        while True:
            self._check_events()
            # Pinta a janela.
            
            self.ship.update()
            
            self._update_screen()

            # Atualiza o ecrã.
            pygame.display.flip()

    def _update_screen(self):
        self.screen.fill(self.bg_color)
        self.ship.blitme()

    def _check_events(self):
        """responder aos eventos do teclado e do rato"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
            elif event.type == pygame.KEYUP:
              if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
              elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False           


    

if __name__ == '__main__':
        #cria uma instancia do jogo e executala.
    ai = AlienInvasion()
    ai.run_game()
