import pygame


class StartScreenView:
    def __init__(self, screen, width, height):
        self._screen = screen
        self._width = width
        self._height = height

        self._colors = {"White": (255, 255, 255), "Black": (0, 0, 0), "Grey": (
            192, 192, 192), "Blue": (0, 0, 128), "Red": (200, 0, 0)}

    def render(self):
        self._screen.fill(self._colors["Black"])

        text_font = pygame.font.SysFont('comicsansms', 64)
        text_content = "Tetris"
        text = text_font.render(text_content, True, self._colors["Blue"])
        rect = text.get_rect()
        pygame.draw.rect(
            self._screen, self._colors["White"], ((self._width - rect[2])//2, 130, rect[2], rect[3]))

        pygame.display.flip()
        self._screen.blit(text, ((self._width - rect[2])//2, 130))

        text_font = pygame.font.SysFont(None, 48)
        text_content = "Press 'Enter' to start playing"
        text = text_font.render(
            text_content, True, self._colors["White"])
        rect = text.get_rect()
        self._screen.blit(text, ((self._width - rect[2])//2, 300))
        pygame.draw.line(
            self._screen, self._colors["White"], ((self._width - rect[2])//2, 300 + rect[3]), ((self._width + rect[2])//2, 300 + rect[3]))

        text_font = pygame.font.SysFont(None, 36)
        text_content = "Press '1' to see game rules"
        text = text_font.render(text_content, True, self._colors["Red"])
        rect = text.get_rect()
        self._screen.blit(text, ((self._width - rect[2])//2, 400))
        pygame.draw.line(
            self._screen, self._colors["White"], ((self._width - rect[2])//2, 400 + rect[3]), ((self._width + rect[2])//2, 400 + rect[3]))

        text_content = "Press '2' to see control options"
        text = text_font.render(text_content, True, self._colors["Red"])
        rect = text.get_rect()
        self._screen.blit(text, ((self._width - rect[2])//2, 450))
        pygame.draw.line(
            self._screen, self._colors["White"], ((self._width - rect[2])//2, 450 + rect[3]), ((self._width + rect[2])//2, 450 + rect[3]))

        text_content = "Press '3' to see high scores"
        text = text_font.render(text_content, True, self._colors["Red"])
        rect = text.get_rect()
        self._screen.blit(text, ((self._width - rect[2])//2, 500))
        pygame.draw.line(
            self._screen, self._colors["White"], ((self._width - rect[2])//2, 500 + rect[3]), ((self._width + rect[2])//2, 500 + rect[3]))

        pygame.display.flip()
