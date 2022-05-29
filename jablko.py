import random
import pygame
import lekcja1

class Jablko():
    #konstruktor klasy
    def __init__(self):
        self.kolor=(193,103,103) #Ustawienie koloru jablka
        self.applePosition=(20,20)
        self.randomPosition() #Losowanie pozycji jablka na poczatku gry
    def setPosition(self,x,y):
        self.applePosition=(x,y)
    def getPosition(self):
        return self.applePosition
    def randomPosition(self):
        ilosckratek=lekcja1.rozdzielczosc//40-1 #Zasieg pojawiania sie jablek zaleznie od rozdzielczosci ekranu
        xApple=random.randint(0,ilosckratek)*40+20 #Losowanie pozycji X jablka
        yApple=random.randint(0,ilosckratek)*40+20 #Losowanie pozycji Y jablka
        self.setPosition(xApple,yApple) #Ustawienie pozycji X i Y jablka
    def drawApple(self,OknoGry): #Rysowanie jablka
        pygame.draw.circle(OknoGry,self.kolor,(self.applePosition[0],self.applePosition[1]),20)