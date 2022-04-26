import pygame
import random
import waz
import jablko

iloscJablek=9
def main():
    objectApple=[]
    for nrApple in range(0,iloscJablek):
        objectApple.append(jablko.Jablko())
    obiektWaz=waz.Snake()
    
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
        
            #rysowanie jabłka
        pygame.draw.circle(OknoGry,(0,255,0),(xApple,yApple),20)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
            #ruch weza
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    obiektWaz.setDirection((0,-1))
                elif event.key == pygame.K_DOWN:
                    obiektWaz.setDirection((0,1))
                elif event.key == pygame.K_LEFT:
                    obiektWaz.setDirection((-1,0))
                elif event.key == pygame.K_RIGHT:
                    obiektWaz.setDirection((1,0))
        #ruch weza        
        obiektWaz.snakeMove()       
        #rysowanie weza
        obiektWaz.drawSnake(OknoGry)        
        #pobranie pozycji glowy weza
        glowa=obiektWaz.pozycje[-1]
        #waż zjada jabłko
        if glowa[0]==xApple-20 and glowa[1]==yApple-20:
            obiektWaz.eating()
            pygame.draw.circle(OknoGry,(255,255,0),(xApple,yApple),20)
            
        
        czcionka=pygame.font.SysFont('comicsans',20)
        tekst=czcionka.render("Punkty: {0}".format(obiektWaz.punkty),1,(255,255,255))
        OknoGry.blit(tekst,(10,10))
        pygame.display.update()

main()