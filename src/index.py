import pygame
#from ui.gameloop import Gameloop
#from ui.event_queue import EventQueue
#from ui.renderer import Renderer
from ui.game import Game
#from entities.clock import Clock
#from entities.field import Field

FIELD = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
CELL_SIZE = 70


def main():
    '''
    Alustaa tarvittavat luokat ja käynnistää ohjelman.
    '''

    #heigth = len(FIELD)
    #width = len(FIELD[0])
    #coefficient = CELL_SIZE//2.5
    #display_heigth = heigth*CELL_SIZE
    #display_width = width*CELL_SIZE

    #pygame.init()
    #screen = pygame.display.set_mode((display_heigth, display_width))
    #pygame.display.set_caption("Tetris")

    #eventqueue = EventQueue()
    #clock = Clock()
    #renderer = Renderer(screen, heigth, width, coefficient, CELL_SIZE)
    #field = Field(FIELD)

    #gameloop = Gameloop(eventqueue, clock, renderer, field)
    #gameloop.start()

    game = Game()
    game.start_screen()

if __name__ == "__main__":
    main()
