import pygame
import sys
from pygame.locals import *
from random import randrange

class Personagem(pygame.sprite.Sprite):
    
    def __init__(self, sprite, pos_x, pos_y, vel_x):
        pygame.sprite.Sprite.__init__(self)
        self.vx = vel_x