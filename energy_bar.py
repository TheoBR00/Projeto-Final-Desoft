import pygame
import sys
from pygame.locals import *
import numpy as np
import random

cronometro = 0


inicio = pygame.init()

pygame.init()
pygame.mixer.init()

# Música obtida por integrante do trabalho
pygame.mixer.music.load("musica jogo.mp3")
pygame.mixer.music.play(1000000000)
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
        self.v_x=per_1.v_x-0.2
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
estado=0
fundo = pygame.image.load("imagem_fundo.png").convert()
telainicial=pygame.image.load("tela_inicial.png").convert()

# Tela de game over obtida em https://pt.aliexpress.com/item/Creative-Game-Over-Wordart-Car-Styling-Stickers-Car-Motocycle-Wall-Home-Glass-Window-Door-Laptop-Black/32791815782.html
gameover=pygame.image.load("game_over.png").convert()
background_size = fundo.get_size()
background_size2 = gameover.get_size()
background_size3 = telainicial.get_size()


per_1 = Personagem(["menino correndo/Run__000.png", "menino correndo/Run__001.png","menino correndo/Run__002.png","menino correndo/Run__003.png","menino correndo/Run__004.png","menino correndo/Run__005.png","menino correndo/Run__006.png", "menino correndo/Run__007.png","menino correndo/Run__008.png","menino correndo/Run__009.png"], 700, 350)
#per_1_j = Personagem(["menino pulando/Jump__000", "menino pulando/Jump__001", "menino pulando/Jump__002", "menino pulando/Jump__003", "menino pulando/Jump__004", "menino pulando/Jump__005", "menino pulando/Jump__006", "menino pulando/Jump__007", "menino pulando/Jump__008", "menino pulando/Jump__009"])
dino = Dinossauro(["dinossauro/Run (1).png", "dinossauro/Run (2).png", "dinossauro/Run (3).png", "dinossauro/Run (4).png", "dinossauro/Run (5).png", "dinossauro/Run (6).png", "dinossauro/Run (7).png", "dinossauro/Run (8).png"], 50, 280,per_1)
obst = obstaculos(["obstaculos/pedra.png", "obstaculos/tronco.png", "obstaculos/caixa.png"], 560, 430,per_1)
lista_obst=["obstaculos/pedra.png", "obstaculos/tronco.png", "obstaculos/caixa.png"]

todos_amigos.add(per_1)
todos_inimigos.add(dino)
relogio = pygame.time.Clock()
#-------------------------------------------------------
#-----------barra de energia--------------
x_barra = 500
y_barra = 50
largura_barra = 300
altura_barra = 40
#desenha a barra no final, tem que por nas ultimas linhas 
#pygame.draw.rect(tela, (0,255,0), (x_barra, y_barra,largura_barra, altura_barra))

#-------------------------------------------------------
timer = True
game_run = True
w,h = background_size
x = 0
y = 0
x1 = w
y1 = 0

pygame.display.set_caption('Dino Run')
dx_cria = 100
t_0 = 0
pont = 0
contra_pont = 0
novo_d_x = 0
dx_cria=1000
distancia=0
maior=0
highscore=[]
velocidade=30
font = pygame.font.SysFont('assets/swiss911.ttf', 50)
font2 = pygame.font.SysFont('assets/swiss911.ttf', 100)



        
while game_run:

    tempo = relogio.tick(velocidade)
        
    if estado==0:
        
        tela.blit(telainicial, (0, 0))
        for event in pygame.event.get():
            if event.type == QUIT:        
                    pygame.mixer.music.stop()
                    game_run = False
            if (event.type==pygame.KEYDOWN):
                if (event.key==pygame.K_RETURN): 
                    estado=1        
    if estado==1:
        
        
        palavra_pontuacao='Pontuação:'
        #palavra_tempo='Tempo:'
        
        pontuacao=str("%.0f"% cronometro)
        
        if timer:
            tempo = str("%.0f" % cronometro)
        #tela.blit(font.render(tempo, True, (0, 0, 0)), (550,25)) #centro
        fonte = pygame.font.SysFont('Consolas', 50)      
        total = str("%.2f" % cronometro)
        
        
                
        if not game_run:
            tempo = False
            timer = False
            if not timer:
               cronometro += 0
               
               
        conta_t = pygame.time.get_ticks()
        conta = (per_1.d_x * 1)/200
        novo_d_x += conta
            
        if per_1.d_x>dx_cria:
            
            obst = obstaculos([random.choice(lista_obst)], 1200, 430,per_1)
            todos_obstaculos.add(obst)
            distancia+=per_1.d_x
            if dx_cria>550:
                dx_cria-=20
            if velocidade<100:
                velocidade+=1
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
            
            estado=2
            
            pygame.mixer.music.stop()
            cronometro=cronometro
            
            
            
            highscore.append(cronometro)
            
            maior=cronometro
            i=0
            while i<len(highscore):
                if highscore[i]>maior:
                    maior=highscore[i]
                    
                i+=1    
            palavra_high_score='High Score:'
            high_score=str("%.0f"% maior)# ate fechar o programa
            
        
        else:    
            
            cronometro += 1
            #cronometro += 1/30
            distancia+=(per_1.d_x/100000000000)
#------------------------------------------------------------------
        #-----------barra de energia--------------    
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                largura_barra -= 10
#------------------------------------------------------------------





            if (event.type==pygame.KEYDOWN):
                if (event.key==pygame.K_SPACE) and per_1.rect.y > 200: 
                    per_1.jump()
            if colisao == True:
                pont += 1
        
        
            elif colisao == False and event.key==pygame.K_SPACE:
                contra_pont -= 1
                
            if event.type == QUIT:
                
                pygame.mixer.music.stop()
                game_run = False

        tela.blit(font2.render(pontuacao, True, (0, 0, 0)), (600,10)) 
        
        todos_amigos.draw(tela)
        todos_obstaculos.update()
        todos_obstaculos.draw(tela)
        todos_obstaculos.draw(tela)
        todos_amigos.update()
        todos_inimigos.update()
        todos_inimigos.draw(tela)
        
        
    elif estado==2:
        enter='Para jogar novamente, aperte Enter'
        tela.blit(gameover, (0, 0))
        tela.blit(font2.render(enter, True, (0, 0, 0)), (30,50))
        tela.blit(font2.render(palavra_high_score, True, (0, 0, 0)), (10,450))
        tela.blit(font2.render(palavra_pontuacao, True, (0, 0, 0)), (800,450))
        tela.blit(font2.render(pontuacao, True, (0, 0, 0)), (1000,530))
        tela.blit(font2.render(high_score, True, (0, 0, 0)), (200,530))
        for event in pygame.event.get():
            if event.type == QUIT:
                
                    pygame.mixer.music.stop()
                    game_run = False
                    
            if (event.type==pygame.KEYDOWN):
                if (event.key==pygame.K_RETURN): 
                    cronometro =0
                    
                    todos_amigos = pygame.sprite.Group()
                    todos_inimigos = pygame.sprite.Group()
                    todos_obstaculos = pygame.sprite.Group()
                    tela = pygame.display.set_mode((1250, 600), 0, 32)
                    estado=0
                    # Tela de fundo obtida em https://www.dreamstime.com/illustration/game-background-2d-game.html?pg=2
                    fundo = pygame.image.load("imagem_fundo.png").convert()
                    telainicial=pygame.image.load("tela_inicial.png").convert()
                    gameover=pygame.image.load("game_over.png").convert()
                    background_size = fundo.get_size()
                    background_size2 = gameover.get_size()
                    background_size3 = telainicial.get_size()
                    
                    # Sprites de menino obtidos em https://www.gameart2d.com/temple-run---free-sprites.html
                    per_1 = Personagem(["menino correndo/Run__000.png", "menino correndo/Run__001.png","menino correndo/Run__002.png","menino correndo/Run__003.png","menino correndo/Run__004.png","menino correndo/Run__005.png","menino correndo/Run__006.png", "menino correndo/Run__007.png","menino correndo/Run__008.png","menino correndo/Run__009.png"], 700, 350)
                    
                    # Sprites de dinossauro obtidos em https://www.gameart2d.com/free-dino-sprites.html
                    dino = Dinossauro(["dinossauro/Run (1).png", "dinossauro/Run (2).png", "dinossauro/Run (3).png", "dinossauro/Run (4).png", "dinossauro/Run (5).png", "dinossauro/Run (6).png", "dinossauro/Run (7).png", "dinossauro/Run (8).png"], 50, 280,per_1)
                    
                    # Sprites de obstáculos obtidos em http://blog.elede.com.br/wp-content/uploads/2016/11/obstaculos-2.0.png
                    obst = obstaculos(["obstaculos/pedra.png", "obstaculos/tronco.png", "obstaculos/caixa.png"], 560, 430,per_1)
                    lista_obst=["obstaculos/pedra.png", "obstaculos/tronco.png", "obstaculos/caixa.png"]
                    
                    todos_amigos.add(per_1)
                    todos_inimigos.add(dino)
                    relogio = pygame.time.Clock()
                    
                    timer = True
                    #-------------------------------------------------------
                    game_run = True
                    w,h = background_size
                    x = 0
                    y = 0
                    x1 = w
                    y1 = 0
                    
                    pygame.display.set_caption('Dino Run')
                    dx_cria = 100
                    t_0 = 0
                    pont = 0
                    contra_pont = 0
                    novo_d_x = 0
                    dx_cria=1000
                    distancia=0
                    velocidade=30
                    font = pygame.font.SysFont('assets/swiss911.ttf', 50)
                    font2 = pygame.font.SysFont('assets/swiss911.ttf', 100)


                    pygame.init()
                    pygame.mixer.init()
                    pygame.mixer.music.load("musica jogo.mp3")
                    pygame.mixer.music.play(1000000000)
        
                    estado=0            
                    
    pygame.display.flip()
            
pygame.display.quit()
