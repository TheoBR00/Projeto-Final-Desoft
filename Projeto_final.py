import pygame
import sys
from pygame.locals import *
import numpy as np
import random

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
        self.d_x= 0
        self.v_y = 0
        self.v_x = 10
   
    def vel(self, velocidade_y,velocidade_x):
        self.v_y = velocidade_y
        self.v_x = velocidade_x
    
    def vida(self, life):
        self.vida = life
    
    def damage(self, dinossauro, personagem, dano):
        for enemy in dinossauro and pygame.sprite.collide(personagem, dinossauro, False):
            enemy.vida -= dano
            
    def jump(self):
        self.v_y = -18 
        self.v_x = 10
             
    def update(self):
        self.atual += 1
        if self.atual >= len(self.imagens):
            self.atual = 0
        self.image = self.imagens[self.atual]
        self.rect.y += self.v_y
        self.v_y += 1
        #self.v_x=10
        self.d_x += self.v_x
        if self.rect.y > 350:
            self.rect.y = 350
            self.v_y = 0
            
class Dinossauro(pygame.sprite.Sprite):
    
    def __init__(self, sprite, pos_x, pos_y,per_1):
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
        self.v_x=per_1.v_x-1
        self.per_1=per_1
    def vel(self, velocidade_x):
        self.v_x = velocidade_x
    
    def update(self):
        self.atual += 1
        if self.atual >= len(self.imagens):
            self.atual = 0
        self.image = self.imagens[self.atual]
        if self.rect.x+35<self.per_1.rect.x :
            self.rect.x+=self.v_x-self.per_1.v_x
        
class obstaculos(pygame.sprite.Sprite):
    
    def __init__(self, sprite, pos_x, pos_y,per_1):
        self.atual = 0
        pygame.sprite.Sprite.__init__(self)
        self.imagens = []
        for imagem in sprite:
            self.image = pygame.image.load(imagem)
            self.imagens.append(self.image)
        self.per_1=per_1    
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.v_x = -10
    
    def update(self):
        self.rect.x -= self.per_1.v_x
        
        
todos_amigos = pygame.sprite.Group()
todos_inimigos = pygame.sprite.Group()
todos_obstaculos = pygame.sprite.Group()
tela = pygame.display.set_mode((1250, 600), 0, 32)
fundo = pygame.image.load("imagem_fundo.png").convert()
background_size = fundo.get_size()

per_1 = Personagem(["menino correndo/Run__000.png", "menino correndo/Run__001.png","menino correndo/Run__002.png","menino correndo/Run__003.png","menino correndo/Run__004.png","menino correndo/Run__005.png","menino correndo/Run__006.png", "menino correndo/Run__007.png","menino correndo/Run__008.png","menino correndo/Run__009.png"], 700, 350)
#per_1_j = Personagem(["menino pulando/Jump__000", "menino pulando/Jump__001", "menino pulando/Jump__002", "menino pulando/Jump__003", "menino pulando/Jump__004", "menino pulando/Jump__005", "menino pulando/Jump__006", "menino pulando/Jump__007", "menino pulando/Jump__008", "menino pulando/Jump__009"])
dino = Dinossauro(["dinossauro/Run (1).png", "dinossauro/Run (2).png", "dinossauro/Run (3).png", "dinossauro/Run (4).png", "dinossauro/Run (5).png", "dinossauro/Run (6).png", "dinossauro/Run (7).png", "dinossauro/Run (8).png"], 50, 280,per_1)
obst = obstaculos(["obstaculos/pedra.png", "obstaculos/tronco.png", "obstaculos/caixa.png"], 560, 430,per_1)
lista_obst=["obstaculos/pedra.png", "obstaculos/tronco.png", "obstaculos/caixa.png"]

todos_amigos.add(per_1)
todos_inimigos.add(dino)
relogio = pygame.time.Clock()


game_run = True
w,h = background_size
x = 0
y = 0
x1 = w
y1 = 0


pygame.display.set_caption('Foge do Dinossauro!')
dx_cria = 100
t_0 = 0
pont = 0
contra_pont = 0
novo_d_x = 0
while game_run:
    tempo = relogio.tick(30)
    conta_t = pygame.time.get_ticks()
    conta = (per_1.d_x * 1.5)/183
    novo_d_x += conta
    if conta_t - t_0 > 300:
        t_0 = conta_t
        dx_cria = 700
    if per_1.d_x>dx_cria:
        obst = obstaculos([random.choice(lista_obst)], 1200, 430,per_1)
        todos_obstaculos.add(obst)
        per_1.d_x= 0
    x1 -= per_1.v_x
    x -= per_1.v_x
    tela.blit(fundo, (x, y))
    tela.blit(fundo, (x1, y1))
   
   
    tela.blit(fundo, (x, y))  
    tela.blit(fundo, (x1, y1))
    if x < -w:
        x = w
    if x1 < -w:
        x1 = w
    colisao = pygame.sprite.collide_mask(per_1,obst)
    colisao_dino = pygame.sprite.collide_mask(dino,per_1)
    if colisao:
        obst.v_x= 0
        per_1.v_x = 0
    else:
        obst.v_x=-10
    
    if colisao_dino:
        print(novo_d_x)
        game_run = False
    for event in pygame.event.get():
        if (event.type==pygame.KEYDOWN):
            if (event.key==pygame.K_SPACE) and per_1.rect.y > 180:
                per_1.jump()
        if colisao == True:
            pont += 1
    
        elif colisao == False and event.key==pygame.K_SPACE:
            contra_pont -= 1
        if event.type == QUIT:
            print(novo_d_x)
            game_run = False
#    tela.blit(fundo, (0, 0))
    
    
    
    todos_amigos.draw(tela)
    
    todos_obstaculos.update()
    todos_obstaculos.draw(tela)
    todos_obstaculos.draw(tela)
    todos_amigos.update()
    todos_inimigos.update()
    todos_inimigos.draw(tela)
    pygame.display.flip()
    pygame.display.update()
        
                
pygame.display.quit()







    
    
    
