import pygame


class Snake():
    #konstruktor klasy
    def __init__(self):
        self.dlugosc=1
        self.punkty=0
        self.pozycje=[(120,120)]
        self.kierunek=(0,1)
    def setDirection(self,kier):
        self.kierunek=kier
    #pobranie pozycji głowy
    def getHead(self):
        return self.pozycje[-1]
    def eating(self):
        self.dlugosc+=1
        self.punkty+=1
    def drawSnake(self,OknoGry):
         for wspolrzendne in self.pozycje[::-1]: 
            wazShape=pygame.Rect((wspolrzendne[0],wspolrzendne[1]),(40,40))
            pygame.draw.rect(OknoGry,(255,192,203),wazShape)
    def snakeMove(self):
        #ostatnia pozycja weza
        ostatniaPozycja=self.pozycje[-1]
        #nowe pozycje
        x=ostatniaPozycja[0]+40*self.kierunek[0]
        y=ostatniaPozycja[1]+40*self.kierunek[1]
        #sprawdzenie przejścia krawędzi
        noweWspl=self.checkBorder(x,y)
         #sprawdzenie czy wąż sam siebie nie zjadł
        for wspol in self.pozycje[::]:
            if noweWspl[0]==wspol[0] and noweWspl[1]==wspol[1]:
                self.pozycje=[]
                self.dlugosc=1
                self.punkty=0
        #dodanie nowej pozycji weza
        self.pozycje.append((noweWspl[0],noweWspl[1]))
        if self.dlugosc<len(self.pozycje):
            del self.pozycje[0]
    #sprawdzenie krawędzi
    def checkBorder(self,zmienna1,zmienna2):
        if zmienna1>=400:
            zmienna1=0
            #przejście dół
        if zmienna2>=400:
            zmienna2=0
        #przejście strona lewa
        if zmienna1<0:
            zmienna1=400
            #przejście góra
        if zmienna2<0:
            zmienna2=400
        return (zmienna1,zmienna2)