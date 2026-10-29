import pygame
class Ship:
    """classe para gerir a nave do jogador"""

    def __init__(self, ai_game):
        """inicializar a nave e definir a sua possiçao inicial"""

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #carregar a imagem da nave 
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #definir a posiçao da nave

        self.rect.midbottom = self.screen_rect.midbottom

        #variaveis de controle de movimento
        self.moving_right = False
        self.moving_left = False


    def update(self):
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1


    def blitme(self):
        """vai desenhar a nave na sua posiçao atual"""

        self.screen.blit(self.image, self.rect)
