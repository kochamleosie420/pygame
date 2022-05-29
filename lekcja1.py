from turtle import pos, position
import pygame #Zaladowanie biblioteki pygame
import random #Zaladowanie biblioteki random
import waz #Zaladowanie pliku waz 
import jablko #Zaladowanie pliku jablko
rozdzielczosc=400
obiektWaz1=waz.Snake()
obiektWaz2=waz.Snake()
def zmienkolorWaz1(color):
    obiektWaz1.setcolor(color)
def zmienkolorWaz2(color):
    obiektWaz2.setcolor(color)
iloscJablek=9
def main(): #Tworzenie funkcji main
    objectApple=[]
    for nrApple in range(0,iloscJablek):
        objectApple.append(jablko.Jablko())
    
    
    xApple=random.randint(0,9)*40+20 #Losowanie liczby od 0 do 9 dla zmiennej
    yApple=random.randint(0,9)*40+20 #Losowanie liczby od 0 do 9 dla zmiennej
    file = 'Soundtrack1.mp3' #Tworzenie zmiennej 
    pygame.init() #zainicjowanie zaimportowanych modułów
    pygame.mixer.init()
    pygame.mixer.music.load(file) #Zaladowanie zmiennej file
    pygame.mixer.music.play(-1) #Loop muzyki
    OknoGry=pygame.display.set_mode((rozdzielczosc, rozdzielczosc),0,32) #Wygenerowanie okna gry do zmiennej
    tlo = pygame.image.load('leosia.png') # Załadowanie obrazka
    tlo = pygame.transform.scale(tlo, (rozdzielczosc, rozdzielczosc)) #Przystosowanie wielkosci obrazka do okna gry
    run=True
    zmienna1=120
    zmienna2=120
    
    while(run):
        OknoGry.fill((0,0,0))
        pygame.time.delay(200) #Spowolnienie ruchu weza
        OknoGry.blit(tlo,(0,0)) #Ustawienie tła

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
            #ruch weza
            elif event.type == pygame.KEYDOWN: #Przypisanie klawiszy do ruchu weza
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
        
        #Liczenie punktów dla obu graczy, ustawienie czcionki
        czcionka=pygame.font.SysFont('comicsans',20)
        tekst1=czcionka.render("Gracz 1: {0}".format(obiektWaz1.punkty),1,(255,255,255))
        OknoGry.blit(tekst1,(10,10))
        tekst2=czcionka.render("Gracz 2: {0}".format(obiektWaz2.punkty),1,(255,255,255))
        OknoGry.blit(tekst2,(10,40))
        pygame.display.update()