import pygame
import sys
from pygame.locals import *
from random import randrange

inicio = pygame.init()

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

todos_amigos = pygame.sprite.Group()
todos_inimigos = pygame.sprite.Group()
tela = pygame.display.set_mode((1238, 491), 0, 32)
fundo = pygame.image.load("fundo-800X600.jpg").convert()
relogio = pygame.time.Clock()


game_run = True


pygame.display.set_caption('Foge do Touro!')
while game_run:
    tempo = relogio.tick(30)
    for event in pygame.event.get():
      if event.type == QUIT:
          game_run = False
    tela.blit(fundo, (0, 0))
    todos_amigos.draw(tela)
    todos_inimigos.draw(tela)
    pygame.display.update()
                
pygame.display.quit()






    
    
    
        
        