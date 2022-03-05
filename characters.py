import pygame
from constants import ARCHERIMAGE, BOXERIMAGE, BRUTEIMAGE, CANNONIMAGE, COMMONERIMAGE, DIAGONALIMAGE, MIMICIMAGE, NINJAIMAGE, SUPPORTIMAGE, TRANSPORTERIMAGE

class Character(pygame.sprite.Sprite):
    def __init__(self, image, rect, identity, level, health, team, index):
        super().__init__()
        self.image = image
        self.rect = rect
        self.identity = identity
        self.level = level
        self.health = health
        self.team = team
        self.index = index
        self.buff = False 
        self.killable = False

all_characters_list = [
Character(BRUTEIMAGE, None, "brute", 4, 3, 0, 0),
Character(CANNONIMAGE, None, "cannon", 4, 3, 0, 1),
Character(ARCHERIMAGE, None, "archer", 3, 2, 0, 2),
Character(BOXERIMAGE, None, "boxer", 3, 3, 0, 3),
Character(SUPPORTIMAGE, None, "support", 3, 2, 0, 4),
Character(DIAGONALIMAGE, None, "diagonal", 2, 1, 0, 5),
Character(MIMICIMAGE, None, "mimic", 2, 2, 0, 6),
Character(NINJAIMAGE, None, "ninja", 2, 1, 0, 7),
Character(TRANSPORTERIMAGE, None, "transporter", 2, 1, 0, 8),
Character(COMMONERIMAGE, None, "commoner", 1, 1, 0, 9)]

all_characters = pygame.sprite.Group(all_characters_list)