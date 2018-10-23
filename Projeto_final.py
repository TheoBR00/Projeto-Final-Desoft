import pygame
import sys
from pygame.locals import *
from random import randrange

class Personagem(pygame.sprite.Sprite):
    
    def __init__(self, sprite, pos_x, pos_y, largura, altura):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(pos_x, pos_y, largura, altura)
        self.image = pygame.image.load(sprite)
        
    def vel(self, velocidade):
        self.v_x = velocidade
    
    def vida(self, life):
        self.vida = life
    
    def damage(self, touro, personagem, dano):
        for enemy in touro and pygame.sprite.collide(personagem, touro, False):
            enemy.vida -= dano

game_run = True

inicio = pygame.init()

tela = pygame.display.set_mode((1238, 491), 0, 32)
pygame.display.set_caption('Foge do Touro!')

game_run = True

fundo = pygame.image.load("fundo-800X600.jpg").convert()
    
    
    
        
        