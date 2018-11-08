import pygame
import sys
from pygame.locals import *
import numpy as np
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
        self.v_y = 0
   
    def vel(self, velocidade):
        self.v_x = velocidade
    
    def vida(self, life):
        self.vida = life
    
    def damage(self, touro, personagem, dano):
        for enemy in touro and pygame.sprite.collide(personagem, touro, False):
            enemy.vida -= dano
            
    def jump(self):
        self.v_y = -14
        
        print(self.rect.y)
            
    
    def update(self):
        self.atual += 1
        if self.atual >= len(self.imagens):
            self.atual = 0
        self.image = self.imagens[self.atual]
        self.rect.y += self.v_y
        self.v_y += 1
        if self.rect.y > 350:
            self.rect.y = 350
            self.v_y = 0
            
class Dinossauro(pygame.sprite.Sprite):
    
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
        self.v_y = 0
   
    def vel(self, velocidade):
        self.v_x = velocidade
    
    def update(self):
        self.atual += 1
        if self.atual >= len(self.imagens):
            self.atual = 0
        self.image = self.imagens[self.atual]
        
       
        

class obstaculos(pygame.sprite.Sprite):
    
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
        self.v_x = -10
    
    def update(self):
        self.rect.x += self.v_x
        
        
    
        

todos_amigos = pygame.sprite.Group()
todos_inimigos = pygame.sprite.Group()
todos_obstaculos = pygame.sprite.Group()
tela = pygame.display.set_mode((1250, 600), 0, 32)
fundo = pygame.image.load("imagem_fundo.png").convert()
background_size = fundo.get_size()

per_1 = Personagem(["menino correndo/Run__000.png", "menino correndo/Run__001.png","menino correndo/Run__002.png","menino correndo/Run__003.png","menino correndo/Run__004.png","menino correndo/Run__005.png","menino correndo/Run__006.png", "menino correndo/Run__007.png","menino correndo/Run__008.png","menino correndo/Run__009.png"], 400, 350)
#per_1_j = Personagem(["menino pulando/Jump__000", "menino pulando/Jump__001", "menino pulando/Jump__002", "menino pulando/Jump__003", "menino pulando/Jump__004", "menino pulando/Jump__005", "menino pulando/Jump__006", "menino pulando/Jump__007", "menino pulando/Jump__008", "menino pulando/Jump__009"])
dino = Dinossauro(["dinossauro/Run (1).png", "dinossauro/Run (2).png", "dinossauro/Run (3).png", "dinossauro/Run (4).png", "dinossauro/Run (5).png", "dinossauro/Run (6).png", "dinossauro/Run (7).png", "dinossauro/Run (8).png"], 10, 280)
obst = obstaculos(["obstaculos/pedra.png", "obstaculos/tronco.png", "obstaculos/caixa.png"], 500, 270)

todos_amigos.add(per_1)
todos_inimigos.add(dino)
todos_obstaculos.add(obst)
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
        if (event.type==pygame.KEYDOWN):
            if (event.key==pygame.K_SPACE):
                per_1.jump()
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
    
    
    todos_amigos.draw(tela)
    
    todos_obstaculos.update()
    todos_obstaculos.draw(tela)
    todos_amigos.update()
    todos_inimigos.update()
    todos_inimigos.draw(tela)
    pygame.display.flip()
    pygame.display.update()
        
                
pygame.display.quit()






    
    
    
        
        