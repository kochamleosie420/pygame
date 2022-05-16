import pygame
import pygame_menu
import lekcja1
import waz
def zmianaRozdzielczosci(nazwaPola,atrybut):
    lekcja1.rozdzielczosc=atrybut
def zmienkolorWaz1(value):
    lekcja1.zmienkolorWaz1(value)
def zmienkolorWaz2(value):
    lekcja1.zmienkolorWaz2(value)
def main():
    pygame.init()
    OknoMenu=pygame.display.set_mode((600,600))
    pygame.display.set_caption("Menu Snake")
    menu = pygame_menu.Menu('Snake 3Ti', 600, 600, theme=pygame_menu.themes.THEME_DARK)
    menu.add.button("Start Gry",lekcja1.main,background_color=(0,0,0))
    menu.add.selector("Rozmiar ekranu",[('400x400',400),('600x600',600),('800x800',800),('1920x1080',1920)],onchange=zmianaRozdzielczosci)
    menu.add.color_input("Kolor weza 1",'rgb', default=(25,25,180),onreturn=zmienkolorWaz1)
    menu.add.color_input("Kolor weza 2",'rgb', default=(25,25,180),onreturn=zmienkolorWaz2)

    menu.mainloop(OknoMenu)

main()