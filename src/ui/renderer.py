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

    def show_start_screen(self):
        '''
        Näyttää sovelluksen aloitusnäkymän
        '''
        self._screen.fill(self._colors["Black"])

        text_font_1 = pygame.font.SysFont('comicsansms', 64)
        text_content_1 = "Tetris"
        text_1 = text_font_1.render(text_content_1, True, self._colors["Blue"])

        rect = text_1.get_rect()
        pygame.draw.rect(self._screen, self._colors["White"], (rect[0] + 580, rect[1] + 130, rect[2], rect[3]))

        pygame.display.flip()

        self._screen.blit(text_1, (580, 130))

        text_font_2 = pygame.font.SysFont(None, 48)
        text_content_2 = "Press 'Enter' to start playing"
        text_2 = text_font_2.render(text_content_2, True, self._colors["White"])

        self._screen.blit(text_2, (520, 300))
        pygame.display.flip()

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

    def draw_field(self, field, block, emptied_rows):
        '''
        Piirtää ruudukon ja poistetut rivit pelin aikana.
        '''
        text_font = pygame.font.SysFont(None, 48)
        text_content = "Cleared lines: "+ str(emptied_rows)
        text = text_font.render(text_content, True, self._colors["Black"])
        rect = text.get_rect()

        pygame.draw.rect(self._screen, self._colors["White"], (rect[0] + (self._height*self._cell_size)*3/4, rect[1] + (self._width*self._cell_size)/3, rect[2], rect[3]))

        self._screen.blit(text, ((self._height*self._cell_size)*3/4, (self._width*self._cell_size)/3))

        for row in range(self._height):
            for column in range(self._width):
                square = ((self._height*self._cell_size)/2-(self._width*self._coefficient/2) + self._coefficient*column, (self._width *
                          self._cell_size)/2 - (self._height*self._coefficient/2) + self._coefficient*row, self._coefficient-1, self._coefficient-1)
                pygame.draw.rect(self._screen, self._colors["Grey"], square)
                if block is not None:
                    for i in block.shape:
                        if row == i[0] + block.row and column == i[1] + block.column:
                            pygame.draw.rect(
                                self._screen, self._colors["Blue"], square)
                if field[row][column] == 1:
                    pygame.draw.rect(self._screen, self._colors["Red"], square)
        pygame.display.flip()
