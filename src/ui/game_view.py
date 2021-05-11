import pygame


class GameView:
    def __init__(self, screen, height, width, coefficient, cell_size):
        self._screen = screen
        self._height = height
        self._width = width
        self._coefficient = coefficient
        self._cell_size = cell_size

        self._colors = {"White": (255, 255, 255), "Black": (0, 0, 0), "Grey": (
            192, 192, 192), "Blue": (0, 0, 128), "Red": (200, 0, 0)}

    def background(self):
        self._screen.fill(self._colors["White"])

        for row in range(self._height):
            for column in range(self._width):
                pygame.draw.rect(self._screen, self._colors["Black"], ((self._height*self._cell_size)/2-(self._width*self._coefficient/2) + self._coefficient*column, (
                    self._width*self._cell_size)/2-(self._height*self._coefficient/2) + self._coefficient*row, self._coefficient, self._coefficient), 1)

        pygame.display.flip()

    def screen(self, field, block, emptied_rows):
        text_font = pygame.font.SysFont(None, 48)
        text_content = "Cleared lines: " + str(emptied_rows)
        text = text_font.render(text_content, True, self._colors["Black"])
        rect = text.get_rect()

        pygame.draw.rect(self._screen, self._colors["White"], (rect[0] + (
            self._height*self._cell_size)*3/4, rect[1] + (self._width*self._cell_size)/3, rect[2], rect[3]))

        self._screen.blit(text, ((self._height*self._cell_size)
                          * 3/4, (self._width*self._cell_size)/3))
        
        text_content = "Press 'P' to pause"
        text = text_font.render(text_content, True, self._colors["Red"])
        self._screen.blit(text, ((self._height*self._cell_size)/10, (self._width*self._cell_size)/3))

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

    def pause(self):
        self._screen.fill(self._colors["Black"])

        text_font = pygame.font.SysFont("comicsansms", 48)
        text_content = "Paused"
        text = text_font.render(text_content, True, self._colors["White"])

        self._screen.blit(text, (600, 300))

        text_font = pygame.font.SysFont(None, 36)
        text_content = "Press 'P' to continue"
        text = text_font.render(text_content, True, self._colors["Red"])

        self._screen.blit(text, (560, 450))
        pygame.display.flip()
