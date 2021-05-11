import pygame

class StartScreenView:
    def __init__(self, screen, height, width, coefficient, cell_size):
        self._screen = screen
        self._height = height
        self._width = width
        self._coefficient = coefficient
        self._cell_size = cell_size

        self._colors = {"White": (255, 255, 255), "Black": (0, 0, 0), "Grey": (
            192, 192, 192), "Blue": (0, 0, 128), "Red": (200, 0, 0)}

    def render(self):
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
