import pygame
from services.gameloop import Gameloop
from services.clock import Clock
from services.block_setter import BlockSetter
from ui.event_queue import EventQueue
from ui.event_handler import EventHandler
from ui.renderer import Renderer
from entities.field import Field

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


class Game:
    '''Luokka, joka siirtelee sovelluksen näkymää alkunäytön, pelisääntöjen, peliohjeiden ja pelitilan välillä.

    Attributes:
        height: Ruudukon korkeus
        width: Ruudukon leveys
        coefficient: Ruudukon kerroin
        display_height: Näytön korkeus
        display_width: Näytön leveys
        screen: Näyttö
        event_queue: EventQueue-olio
        clock: Clock-olio
        renderer: Renderer-olio
        field: Field-olio
        block_setter: BlockSetter-olio
        gameloop: Gameloop-olio
    '''

    def __init__(self):
        '''Luokan konstruktori, joka alustaa kaikki tarvittavat oliot näytön näyttämistä ja uuden pelikierroksen aloittamista varten.
        '''

        self._height = len(FIELD)
        self._width = len(FIELD[0])
        self._coefficient = CELL_SIZE//2.5
        self._display_height = self._height*CELL_SIZE
        self._display_width = self._width*CELL_SIZE

        pygame.init()
        self._screen = pygame.display.set_mode(
            (self._display_height, self._display_width))
        pygame.display.set_caption("Tetris")

        self._event_queue = EventQueue()
        self._event_handler = EventHandler()
        self._clock = Clock()
        self._renderer = Renderer(
            self._screen, self._height, self._width, self._coefficient, CELL_SIZE)
        self._field = Field(FIELD)
        self._block_setter = BlockSetter()
        self._gameloop = Gameloop(
            self._event_queue, self._event_handler, self._clock, self._renderer, self._field, self._block_setter)

    def start_screen(self):
        '''Näyttää aloitusnäytön ja siirtyy muihin käyttöliittymän tiloihin käyttäjän syötteen perusteella'''
        self._renderer.show_start_screen()

        while True:
            event = self._event_queue.get()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    score = self._gameloop.start()
                    break

                if event.key == pygame.K_1:
                    self._renderer.show_game_rules(self._event_queue)
                    break

                if event.key == pygame.K_2:
                    self._renderer.show_control_options(self._event_queue)
                    break

            elif event.type == pygame.QUIT:
                exit()

        self.initialize()
        self.start_screen()

    def initialize(self):
        '''Alustaa ruudukon uutta pelikierrosta varten'''
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
        self._field = Field(FIELD)
        self._gameloop = Gameloop(
            self._event_queue, self._event_handler, self._clock, self._renderer, self._field, self._block_setter)
