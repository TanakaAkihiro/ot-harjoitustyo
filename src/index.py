import pygame
from ui.game import Gameloop

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 520))

    pygame.display.set_caption("Tetris")

    gameloop = Gameloop(screen, 20, 10)
    gameloop.start()

if __name__=="__main__":
    main()