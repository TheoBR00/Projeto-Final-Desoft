import pygame
from random import randint

branco=(255,255,255)
preto=(0,0,0)
vermelho=(255,0,0)
verde=(0,255,0)
azul=(0,0,255)
i = 0
try:
    pygame.init()
except:
    print("O modulo pygame não foi inicializado com sucesso")
relogio = pygame.time.Clock() #relogio para definir fps

largura=500
altura=500
tamanho = 10
pos_x = altura/2
pos_y = largura/2
velocidade_x=0
velocidade_y=0

fundo = pygame.display.set_mode((largura,altura))
pygame.display.set_caption("Snake")

sair = True

while sair:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sair = False
        if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and velocidade_x != tamanho:
                        pos_x += i 

            
    fundo.fill(branco)
    pygame.draw.rect(fundo, preto, [pos_x,pos_y,tamanho,tamanho])
    pos_x+=velocidade_x
    relogio.tick(15)
    pygame.display.update()
    i += 1

pygame.quit()

