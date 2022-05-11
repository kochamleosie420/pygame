import random
import pygame
import lekcja1

class Jablko():
    #konstruktor klasy
    def __init__(self):
        self.kolor=(193,103,103)
        self.applePosition=(20,20)
        self.randomPosition()
    def setPosition(self,x,y):
        self.applePosition=(x,y)
    def getPosition(self):
        return self.applePosition
    def randomPosition(self):
        ilosckratek=lekcja1.rozdzielczosc//40-1
        xApple=random.randint(0,ilosckratek)*40+20
        yApple=random.randint(0,ilosckratek)*40+20
        self.setPosition(xApple,yApple)
    def drawApple(self,OknoGry):
        pygame.draw.circle(OknoGry,self.kolor,(self.applePosition[0],self.applePosition[1]),20)