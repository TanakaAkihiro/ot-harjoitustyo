import pygame


class Renderer:

    '''
    Luokka, joka käsittelee näytön piirtämistä.
    '''

    def __init__(self, screen, height, width, coefficient, cell_size):
        self._screen = screen
        self._height = height
        self._width = width
        self._coefficient = coefficient
        self._cell_size = cell_size

        self._colors = {"White": (255, 255, 255), "Black": (0, 0, 0), "Grey": (
            192, 192, 192), "Blue": (0, 0, 128), "Red": (200, 0, 0)}

    def show_screen(self):
        '''
        Piirtää valkoisen taustan sekä ruudukon.
        '''

        self._screen.fill(self._colors["White"])

        for row in range(self._height):
            for column in range(self._width):
                pygame.draw.rect(self._screen, self._colors["Black"], ((self._height*self._cell_size)/2-(self._width*self._coefficient/2) + self._coefficient*column, (
                    self._width*self._cell_size)/2-(self._height*self._coefficient/2) + self._coefficient*row, self._coefficient, self._coefficient), 1)

        pygame.display.flip()

    def draw_field(self, field, block):
        '''
        Piirtää ruudukon pelin aikana.
        '''

        for row in range(self._height):
            for column in range(self._width):
                square = ((self._height*self._cell_size)/2-(self._width*self._coefficient/2) + self._coefficient*column, (self._width *
                          self._cell_size)/2 - (self._height*self._coefficient/2) + self._coefficient*row, self._coefficient-1, self._coefficient-1)
                pygame.draw.rect(self._screen, self._colors["Grey"], square)
                if block is not None:
                    for i in block.shape:
                        if row == i[0] + block.row and column == i[1] + block.column:
                            pygame.draw.rect(self._screen, self._colors["Blue"], square)
                if field[row][column] == 1:
                    pygame.draw.rect(self._screen, self._colors["Red"], square)
        pygame.display.flip()
