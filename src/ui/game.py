import pygame
from services.gameloop import Gameloop
from services.clock import Clock
from services.block_setter import BlockSetter
from ui.event_queue import EventQueue
from ui.event_handler import EventHandler
from ui.renderer import Renderer
from entities.field import Field
from repositories.score_repository import (
    score_repository as default_score_repository)

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
        score_repository: ScoreRepository-olio
        gameloop: Gameloop-olio
        '''

    def __init__(self, score_repository=default_score_repository):
        '''Luokan konstruktori, joka alustaa kaikki tarvittavat oliot näytön näyttämistä ja uuden pelikierroksen aloittamista varten.

        Args:
            score_repository: ScoreRepository
        '''

        self._height = len(FIELD)
        self._width = len(FIELD[0])
        self._coefficient = CELL_SIZE//2.5
        self._display_height = self._width*CELL_SIZE
        self._display_width = self._height*CELL_SIZE

        pygame.init()
        self._screen = pygame.display.set_mode(
            (self._display_width, self._display_height))
        pygame.display.set_caption("Tetris")

        self._score_repository = score_repository
        self._event_queue = EventQueue()
        self._event_handler = EventHandler()
        self._clock = Clock()
        self._renderer = Renderer(
            self._screen, self._height, self._width, self._coefficient, CELL_SIZE, self._score_repository, self._clock, self._event_handler, self._event_queue)
        self._field = Field(FIELD)
        self._block_setter = BlockSetter()
        self._gameloop = Gameloop(
            self._event_queue, self._event_handler, self._clock, self._renderer, self._field, self._block_setter)

    def start_screen(self):
        '''Näyttää aloitusnäytön ja siirtyy muihin käyttöliittymän tiloihin käyttäjän syötteen perusteella'''
        self._renderer.show_start_screen()

        score = self._event_handler.handle_menu_events(
            self._event_queue, self._renderer, self._gameloop)

        if score == "DELETE":
            self._score_repository.delete_all()
        elif score:
            self._score_repository.add_new_score(score[0], score[1])

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
