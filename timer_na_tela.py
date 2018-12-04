pygame.display.set_caption('Foge do Dinossauro!')
font = pygame.font.SysFont('assets/swiss911.ttf', 40)
while game_run:
    #tempo = str("%.2f" % cronometro)
    #tela.blit(font.render(tempo, True, (0, 0, 0)), (550,25))
    #pygame.display.update()
    if timer:
        tempo = str("%.2f" % cronometro)
        tela.blit(font.render(tempo, True, (0, 0, 0)), (550,25))
        font = pygame.font.SysFont('Consolas', 50)      
        total = str("%.2f" % cronometro)
        #tela.blit(font.render(tempo, True, (0, 0, 0)), (50,50))
        pygame.display.update()
                
        if not game_run:
            #cronometro = Pause  
            timer = False
            if timer:
                cronometro += 1/30