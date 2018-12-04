cronometro = 0
timer = True
font = pygame.font.SysFont('assets/swiss911.ttf', 40)
        
        tempo = str("%.2f" % cronometro)
        tela.blit(font.render(tempo, True, (0, 0, 0)), (550,25))
        pygame.display.update()   
        if timer:
            
                font = pygame.font.SysFont('Consolas', 50)      
                total = str("%.2f" % cronometro)
                tela.blit(font.render(tempo, True, (0, 0, 0)), (50,50))
                pygame.display.update()
                
            if not game_run
               #cronometro = Pause  
               timer = False
            if timer:
        cronometro += 1/30