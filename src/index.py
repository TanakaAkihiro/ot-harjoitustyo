import pygame
from ui.gameloop import Gameloop
from entities.clock import Clock
from ui.event_queue import EventQueue
from ui.renderer import Renderer

FIELD = [
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0]
        ]
CELL_SIZE = 70



def main():
    heigth = len(FIELD)
    width = len(FIELD[0])
    coefficient = CELL_SIZE//2.5
    display_heigth = heigth*CELL_SIZE
    display_width = width*CELL_SIZE

    pygame.init()
    screen = pygame.display.set_mode((display_heigth, display_width))
    pygame.display.set_caption("Tetris")

    eventqueue = EventQueue()
    clock = Clock()
    renderer = Renderer(screen, heigth, width, coefficient, CELL_SIZE)

    gameloop = Gameloop(screen, heigth, width, coefficient, eventqueue, clock, renderer, FIELD)
    gameloop.start()

if __name__=="__main__":
    main()