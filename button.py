import pygame
from constants import *

ready_button_rect = pygame.Rect(WIDTH/1.2, HEIGHT/5, 180, 120)

class Button(pygame.sprite.Sprite):
    def __init__(self, image, rect=None, text=''):
        super().__init__()
        self.image = image
        self.rect = rect
        self.text = text
    
    def draw(self,win,outline=None):
    #Call this method to draw the button on the screen
        if self.rect!= None:
            pygame.draw.rect(SCREEN, RED, self.rect)
        
        if self.text != '':
            font = pygame.font.SysFont('comicsans', 60)
            text = font.render(self.text, 1, (0,0,0))
            SCREEN.blit(text, self.rect)