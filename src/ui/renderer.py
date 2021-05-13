import pygame
from ui.start_screen_view import StartScreenView
from ui.game_rules_view import GameRulesView
from ui.control_options_view import ControlOptionsView
from ui.ranking_view import RankingView
from ui.game_view import GameView

class Renderer:

    '''Luokka, joka käsittelee näytön piirtämistä.

    Attributes:
        screen: Näyttö
        height: Ruudukon korkeus
        width: Ruudukon leveys
        coefficient: Ruudukon kerroin
        cell_size: Näytön kerroin
        colors: Sanakirja väreille
    '''

    def __init__(self, screen, height, width, coefficient, cell_size, score_repository):
        '''Luokan konstruktori, joka luo uuden näytön piirtäjän

        Args:
            screen: Näyttö
            height: Ruudukon korkeus
            width: Ruudukon leveys
            coefficient: Ruudukon kerroin
            cell_size: Näytön kerroin
        '''
        self._screen = screen
        self._height = height
        self._width = width
        self._coefficient = coefficient
        self._cell_size = cell_size
        self._score_repository = score_repository

        self._colors = {"White": (255, 255, 255), "Black": (0, 0, 0), "Grey": (
            192, 192, 192), "Blue": (0, 0, 128), "Red": (200, 0, 0)}

        self._current_view = None

    def show_start_screen(self):
        '''Näyttää sovelluksen aloitusnäkymän
        '''
        self._current_view = StartScreenView(self._screen, self._height*self._cell_size, self._width*self._cell_size)
        self._current_view.render()

    def show_game_rules(self):
        '''Näyttää pelisäännöt
        '''
        self._current_view = GameRulesView(self._screen, self._height*self._cell_size, self._width*self._cell_size)
        self._current_view.render()        

    def show_control_options(self):
        '''Näyttää peliohjeet
        '''
        self._current_view = ControlOptionsView(self._screen, self._height*self._cell_size, self._width*self._cell_size)
        self._current_view.render()
    
    def show_ranking(self):
        '''Näyttää kymmenen parasta pelitulosta
        '''
        self._current_view = RankingView(self._screen, self._height*self._cell_size, self._width*self._cell_size, self._score_repository)
        self._current_view.render()

    def show_game_background(self):
        '''Piirtää valkoisen taustan ja ruudukon.
        '''
        self._current_view = GameView(self._screen, self._height, self._width, self._coefficient, self._cell_size)
        self._current_view.background()

    def draw_field(self, field, block, emptied_rows):
        '''Piirtää ruudukon pelin aikana.

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
