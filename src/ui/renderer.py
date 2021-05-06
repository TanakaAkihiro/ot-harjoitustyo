import pygame


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

    def __init__(self, screen, height, width, coefficient, cell_size):
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

        self._colors = {"White": (255, 255, 255), "Black": (0, 0, 0), "Grey": (
            192, 192, 192), "Blue": (0, 0, 128), "Red": (200, 0, 0)}

    def show_start_screen(self):
        '''Näyttää sovelluksen aloitusnäkymän
        '''
        self._screen.fill(self._colors["Black"])

        text_font_1 = pygame.font.SysFont('comicsansms', 64)
        text_content_1 = "Tetris"
        text_1 = text_font_1.render(text_content_1, True, self._colors["Blue"])

        rect = text_1.get_rect()
        pygame.draw.rect(
            self._screen, self._colors["White"], (rect[0] + 580, rect[1] + 130, rect[2], rect[3]))

        pygame.display.flip()

        self._screen.blit(text_1, (580, 130))

        text_font_2 = pygame.font.SysFont(None, 48)
        text_content_2 = "Press 'Enter' to start playing"
        text_2 = text_font_2.render(
            text_content_2, True, self._colors["White"])

        self._screen.blit(text_2, (450, 300))
        pygame.draw.line(
            self._screen, self._colors["White"], (450, 330), (895, 330))

        text_font_3 = pygame.font.SysFont(None, 36)
        text_content_3 = "Press '1' to see game rules"
        text_3 = text_font_3.render(text_content_3, True, self._colors["Red"])

        self._screen.blit(text_3, (515, 400))
        pygame.draw.line(
            self._screen, self._colors["White"], (515, 423), (825, 423))

        text_font_4 = pygame.font.SysFont(None, 36)
        text_content_4 = "Press '2' to see control options"
        text_4 = text_font_4.render(text_content_4, True, self._colors["Red"])

        self._screen.blit(text_4, (492, 450))
        pygame.draw.line(
            self._screen, self._colors["White"], (492, 473), (852, 473))

        pygame.display.flip()

    def show_game_rules(self):
        '''Näyttää pelisäännöt

        Args:
            event_queue: EventQueue-olio, jonka avulla pääsee pelisäännön näkymästä alkunäyttöön
        '''
        self._screen.fill(self._colors["Black"])

        text_font = pygame.font.SysFont(None, 36)
        text_content = "Players complete lines by moving differently shaped pieces, which descend onto the playing field."
        text = text_font.render(text_content, True, self._colors["White"])
        self._screen.blit(text, (120, 200))

        text_content = "The completed lines disappear and grant the player points, and the player can proceed to fill the vacated spaces."
        text = text_font.render(text_content, True, self._colors["White"])
        self._screen.blit(text, (40, 300))

        text_content = "The game ends when the playing field is filled."
        text = text_font.render(text_content, True, self._colors["White"])
        self._screen.blit(text, (425, 400))

        text_content = "Reference: Wikipedia (2021), https://en.wikipedia.org/wiki/Tetris"
        text = text_font.render(text_content, True, self._colors["White"])
        self._screen.blit(text, (650, 600))

        text_content = "Press 'R' to return"
        text = text_font.render(text_content, True, self._colors["Red"])
        self._screen.blit(text, (30, 600))

        pygame.display.flip()

    def show_control_options(self):
        '''Näyttää peliohjeet

        Args:
            event_queue: EventQueue-olio, jonka avulla pystyy palaamaan alkunäyttöön
        '''
        self._screen.fill(self._colors["Black"])

        text_font = pygame.font.SysFont(None, 48)
        text_content = "OPTIONS"
        text = text_font.render(text_content, True, self._colors["White"])
        self._screen.blit(text, (600, 50))

        text_font = pygame.font.SysFont(None, 36)
        text_content = "MOVE RIGHT:"
        text = text_font.render(text_content, True, self._colors["White"])
        self._screen.blit(text, (400, 200))

        text_content = "RIGHT ARROW"
        text = text_font.render(text_content, True, self._colors["Blue"])
        self._screen.blit(text, (800, 200))

        text_content = "MOVE LEFT:"
        text = text_font.render(text_content, True, self._colors["White"])
        self._screen.blit(text, (400, 250))

        text_content = "LEFT ARROW"
        text = text_font.render(text_content, True, self._colors["Blue"])
        self._screen.blit(text, (800, 250))

        text_content = "ROTATE RIGHT:"
        text = text_font.render(text_content, True, self._colors["White"])
        self._screen.blit(text, (400, 300))

        text_content = "UP ARROW"
        text = text_font.render(text_content, True, self._colors["Blue"])
        self._screen.blit(text, (800, 300))

        text_content = "ROTATE LEFT:"
        text = text_font.render(text_content, True, self._colors["White"])
        self._screen.blit(text, (400, 350))

        text_content = "Z"
        text = text_font.render(text_content, True, self._colors["Blue"])
        self._screen.blit(text, (800, 350))

        text_content = "SOFT DROP:"
        text = text_font.render(text_content, True, self._colors["White"])
        self._screen.blit(text, (400, 400))

        text_content = "DOWN ARROW"
        text = text_font.render(text_content, True, self._colors["Blue"])
        self._screen.blit(text, (800, 400))

        text_content = "Press 'R' to return"
        text = text_font.render(text_content, True, self._colors["Red"])
        self._screen.blit(text, (100, 600))

        pygame.display.flip()

    def show_screen(self):
        '''Piirtää valkoisen taustan ja ruudukon.
        '''

        self._screen.fill(self._colors["White"])

        for row in range(self._height):
            for column in range(self._width):
                pygame.draw.rect(self._screen, self._colors["Black"], ((self._height*self._cell_size)/2-(self._width*self._coefficient/2) + self._coefficient*column, (
                    self._width*self._cell_size)/2-(self._height*self._coefficient/2) + self._coefficient*row, self._coefficient, self._coefficient), 1)

        pygame.display.flip()

    def draw_field(self, field, block, emptied_rows):
        '''Piirtää ruudukon pelin aikana.

        Args:
            field: Field-olio
            block: Block-olio
            emptied_rows: Tyhjennettyjen rivien määrä
        '''
        text_font = pygame.font.SysFont(None, 48)
        text_content = "Cleared lines: " + str(emptied_rows)
        text = text_font.render(text_content, True, self._colors["Black"])
        rect = text.get_rect()

        pygame.draw.rect(self._screen, self._colors["White"], (rect[0] + (
            self._height*self._cell_size)*3/4, rect[1] + (self._width*self._cell_size)/3, rect[2], rect[3]))

        self._screen.blit(text, ((self._height*self._cell_size)
                          * 3/4, (self._width*self._cell_size)/3))

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
