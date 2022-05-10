from turtle import pos, position
import pygame
import random
import waz
import jablko

iloscJablek=9
def main():
    objectApple=[]
    for nrApple in range(0,iloscJablek):
        objectApple.append(jablko.Jablko())
    obiektWaz1=waz.Snake()
    obiektWaz2=waz.Snake()
    
    xApple=random.randint(0,9)*40+20
    yApple=random.randint(0,9)*40+20
    pygame.init()
    OknoGry=pygame.display.set_mode((400,400),0,32)
    run=True
    zmienna1=120
    zmienna2=120
    
    while(run):
        OknoGry.fill((0,0,0))
        pygame.time.delay(200)
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
            #ruch weza
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    obiektWaz1.setDirection((0,-1))
                elif event.key == pygame.K_DOWN:
                    obiektWaz1.setDirection((0,1))
                elif event.key == pygame.K_LEFT:
                    obiektWaz1.setDirection((-1,0))
                elif event.key == pygame.K_RIGHT:
                    obiektWaz1.setDirection((1,0))

                elif event.key == pygame.K_w:
                    obiektWaz2.setDirection((0,-1))
                elif event.key == pygame.K_s:
                    obiektWaz2.setDirection((0,1))
                elif event.key == pygame.K_a:
                    obiektWaz2.setDirection((-1,0))
                elif event.key == pygame.K_d:
                    obiektWaz2.setDirection((1,0))
        #ruch weza        
        obiektWaz1.snakeMove()  
        obiektWaz2.snakeMove()      
        #rysowanie weza
        obiektWaz1.drawSnake(OknoGry)  
        obiektWaz2.drawSnake(OknoGry)        
        #pobranie pozycji glowy weza
        glowa1=obiektWaz1.pozycje[-1]
        glowa2=obiektWaz2.pozycje[-1]
        #waż zjada jabłko
        for nrApple in objectApple[::]:
                positionApple=nrApple.getPosition()
                if glowa1[0]==positionApple[0]-20 and glowa1[1]==positionApple[1]-20:
                    obiektWaz1.eating()
                    nrApple.randomPosition()
                if glowa2[0]==positionApple[0]-20 and glowa2[1]==positionApple[1]-20:
                    obiektWaz2.eating()
                    nrApple.randomPosition()                    
        #Rysowanie jabłka
                nrApple.drawApple(OknoGry)
        #Zjadanie sie wezy nawzajem
        obiektWaz1.biteMe(glowa2)
        obiektWaz2.biteMe(glowa1)
        
        czcionka=pygame.font.SysFont('comicsans',20)
        tekst1=czcionka.render("Gracz 1: {0}".format(obiektWaz1.punkty),1,(255,255,255))
        OknoGry.blit(tekst1,(10,10))
        tekst2=czcionka.render("Gracz 2: {0}".format(obiektWaz2.punkty),1,(255,255,255))
        OknoGry.blit(tekst2,(10,40))
        pygame.display.update()