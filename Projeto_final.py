import pygame
import sys
from pygame.locals import *
from random import randrange

inicio = pygame.init()

class Personagem(pygame.sprite.Sprite):
    
    def __init__(self, sprite, pos_x, pos_y):
        self.atual = 0
        pygame.sprite.Sprite.__init__(self)
        self.imagens = []
        for imagem in sprite:
            self.image = pygame.image.load(imagem)
            self.imagens.append(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
   
    def vel(self, velocidade):
        self.v_x = velocidade
    
    def vida(self, life):
        self.vida = life
    
    def damage(self, touro, personagem, dano):
        for enemy in touro and pygame.sprite.collide(personagem, touro, False):
            enemy.vida -= dano
    
    def update(self):
        self.atual += 1
        if self.atual >= len(self.imagens):
            self.atual = 0
        self.image = self.imagens[self.atual]
        


todos_amigos = pygame.sprite.Group()
todos_inimigos = pygame.sprite.Group()
tela = pygame.display.set_mode((800, 600), 0, 32)
fundo = pygame.image.load("imagem_fundo.png").convert()
background_size = fundo.get_size()
per_1 = Personagem(["menino correndo/Run__000.png", "menino correndo/Run__001.png","menino correndo/Run__002.png","menino correndo/Run__003.png","menino correndo/Run__004.png","menino correndo/Run__005.png","menino correndo/Run__006.png", "menino correndo/Run__007.png","menino correndo/Run__008.png","menino correndo/Run__009.png"], 300, 350)
todos_amigos.add(per_1)
relogio = pygame.time.Clock()


game_run = True
w,h = background_size
x = 0
y = 0
x1 = w
y1 = 0


pygame.display.set_caption('Foge do Touro!')
while game_run:
    tempo = relogio.tick(30)
    for event in pygame.event.get():
      if event.type == QUIT:
          game_run = False
#    tela.blit(fundo, (0, 0))
    x1 -= 10
    x -= 10
    tela.blit(fundo, (x, y))
    tela.blit(fundo, (x1, y1))
    if x < -w:
        x = w
    if x1 < -w:
        x1 = w
#    pygame.display.update()
    
    
    
    todos_amigos.draw(tela)
    todos_inimigos.draw(tela)
    todos_amigos.update()
    todos_inimigos.update()
    pygame.display.flip()
    pygame.display.update()
        
                
pygame.display.quit()






    
    
    
        
        