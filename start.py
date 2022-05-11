import pygame
import pygame_menu
import lekcja1
def zmianaRozdzielczosci(nazwaPola,atrybut):
    lekcja1.rozdzielczosc=atrybut
def main():
    pygame.init()
    OknoMenu=pygame.display.set_mode((400,400))
    pygame.display.set_caption("Menu Snake")
    menu = pygame_menu.Menu('Snake 3Ti', 400, 400, theme=pygame_menu.themes.THEME_DARK)
    menu.add.button("Start Gry",lekcja1.main,background_color=(0,0,0))
    menu.add.selector("Rozmiar ekranu",[('400x400',400),('600x600',600),('800x800',800),('1920x1080',1920)],onchange=zmianaRozdzielczosci)

    menu.mainloop(OknoMenu)

main()