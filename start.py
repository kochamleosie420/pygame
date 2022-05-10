import pygame
import pygame_menu
import lekcja1

def main():
    pygame.init()
    OknoMenu=pygame.display.set_mode((400,400))
    pygame.display.set_caption("Menu Snake")
    menu = pygame_menu.Menu('Snake 3Ti', 400, 400, theme=pygame_menu.themes.THEME_DARK)
    menu.add.button("Start Gry",lekcja1.main,background_color=(0,0,0))

    menu.mainloop(OknoMenu)

main()