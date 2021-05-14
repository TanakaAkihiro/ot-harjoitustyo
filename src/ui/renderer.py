import pygame
from ui.start_screen_view import StartScreenView
from ui.game_rules_view import GameRulesView
from ui.control_options_view import ControlOptionsView
from ui.high_scores_view import HighScoresView
from ui.game_view import GameView
from ui.new_score_view import NewScoreView


class Renderer:

    '''Luokka, joka käsittelee näytön piirtämistä.

    Attributes:
        screen: Näyttö
        height: Ruudukon korkeus
        width: Ruudukon leveys
        coefficient: Ruudukon kerroin
        cell_size: Näytön kerroin
        score_repository: ScoreRepository-olio
        clock: Clock-olio
        event_handler: EventHandler-olio
        event_queue: EventQueue-olio
        colors: Sanakirja väreille
        current_view: Muuttuja, jonka arvoksi määrätään halutun näkymän olio
    '''

    def __init__(self, screen, height, width, coefficient, cell_size, score_repository, clock, event_handler, event_queue):
        '''Luokan konstruktori, joka luo uuden näytön piirtäjän

        Args:
            screen: Näyttö
            height: Ruudukon korkeus
            width: Ruudukon leveys
            coefficient: Ruudukon kerroin
            cell_size: Näytön kerroin
            score_repository: ScoreRepository-olio
            clock: Clock-olio
            event_handler: EventHandler-olio
            event_queue: EventQueue-olio
        '''
        self._screen = screen
        self._height = height
        self._width = width
        self._coefficient = coefficient
        self._cell_size = cell_size
        self._score_repository = score_repository
        self._clock = clock
        self._event_handler = event_handler
        self._event_queue = event_queue

        self._colors = {"White": (255, 255, 255), "Black": (0, 0, 0), "Grey": (
            192, 192, 192), "Blue": (0, 0, 128), "Red": (200, 0, 0)}

        self._current_view = None

    def show_start_screen(self):
        '''Näyttää sovelluksen aloitusnäkymän
        '''
        self._current_view = StartScreenView(
            self._screen, self._height*self._cell_size, self._width*self._cell_size)
        self._current_view.render()

    def show_game_rules(self):
        '''Näyttää pelisäännöt
        '''
        self._current_view = GameRulesView(
            self._screen, self._height*self._cell_size, self._width*self._cell_size)
        self._current_view.render()

    def show_control_options(self):
        '''Näyttää pelin ohjeet
        '''
        self._current_view = ControlOptionsView(
            self._screen, self._height*self._cell_size, self._width*self._cell_size)
        self._current_view.render()

    def show_high_scores(self):
        '''Näyttää kymmenen parasta pelitulosta
        '''
        self._current_view = HighScoresView(
            self._screen, self._height*self._cell_size, self._width*self._cell_size, self._score_repository)
        self._current_view.render()

    def show_game_background(self):
        '''Piirtää valkoisen taustan ja ruudukon.
        '''
        self._current_view = GameView(
            self._screen, self._height, self._width, self._coefficient, self._cell_size)
        self._current_view.background()

    def draw_field(self, field, block, emptied_rows):
        '''Piirtää ruutuja ruudukkoon pelin aikana.

        Args:
            field: Field-olio
            block: Block-olio
            emptied_rows: Tyhjennettyjen rivien määrä
        '''
        self._current_view.screen(field, block, emptied_rows)

    def show_pause(self):
        '''Näyttää pause-näytön
        '''
        self._current_view.pause()

    def save_new_score(self, score):
        '''Pelin tuloksen tallentamisen näkymä

        Args:
            score: Pelikierroksen tulos

        Returns:
            Pelaajan nimen merkkijonona
        '''
        self._current_view = NewScoreView(self._screen, self._height*self._cell_size, self._width*self._cell_size, score, self._clock, self._event_handler, self._event_queue)
        return self._current_view.render()