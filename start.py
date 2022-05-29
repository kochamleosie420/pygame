import pygame
import pygame_menu
import lekcja1
import waz
def iloscJablek(value,ilosc):
    lekcja1.iloscJablek=ilosc
def zmianaRozdzielczosci(nazwaPola,atrybut): 
    lekcja1.rozdzielczosc=atrybut
def zmienkolorWaz1(value): #funkcja zmieniajaca kolor weza 1 zaladowana z pliku lekcja1.py
    lekcja1.zmienkolorWaz1(value)
def zmienkolorWaz2(value):  
    lekcja1.zmienkolorWaz2(value) #funkcja zmieniajaca kolor weza 2 zaladowana z pliku lekcja1.py
def main():
    pygame.init()
    OknoMenu=pygame.display.set_mode((600,600)) #Ustawienie wielkosci okna menu
    pygame.display.set_caption("Menu Snake") #Wyswietlenie nazwy okna
    menu = pygame_menu.Menu('Snake 3Ti', 600, 600, theme=pygame_menu.themes.THEME_DARK) #Dopasowanie menu do wielkosci okna menu , ustawienie nazwy oraz motywu
    menu.add.button("Start Gry",lekcja1.main,background_color=(0,0,0)) #Dodanie przycisku start gry , który uruchamia lekcja1.main oraz ustawia kolor tla przycisku na czarny
    menu.add.selector("Rozmiar ekranu",[('400x400',400),('600x600',600),('800x800',800)],onchange=zmianaRozdzielczosci)  #Dodanie przycisku z mozliwoscia zmiany rozdzielczosci okna gry
    menu.add.color_input("Kolor weza 1",'rgb', default=(25,25,180),onreturn=zmienkolorWaz1)  #Dodanie przycisku z mozliwoscia zmiany koloru weza nr 1 , w rgb
    menu.add.color_input("Kolor weza 2",'rgb', default=(25,25,180),onreturn=zmienkolorWaz2) #Dodanie przycisku z mozliwoscia zmiany koloru weza nr 2 , w rgb
    menu.add.selector("Ilosc jablek",[("1",1),("3",3),("10",10),("20",20),("50",50)],onchange=iloscJablek) #Dodanie przycisku z mozliwoscia zmiany ilosci jablek

    menu.mainloop(OknoMenu) #Powtarzanie czynnosci dopoki uzytkownik nie wyjdzie z okna

main()