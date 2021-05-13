import pygame


class GameRulesView:
    def __init__(self, screen, width, height):
        self._screen = screen
        self._width = width
        self._height = height

        self._colors = {"White": (255, 255, 255), "Black": (0, 0, 0), "Grey": (
            192, 192, 192), "Blue": (0, 0, 128), "Red": (200, 0, 0)}

    def render(self):
        self._screen.fill(self._colors["Black"])

        text_font = pygame.font.SysFont(None, 36)
        text_content = "Players complete lines by moving differently shaped pieces, which descend onto the playing field."
        text = text_font.render(text_content, True, self._colors["White"])
        rect = text.get_rect()
        self._screen.blit(text, ((self._width - rect[2])//2, 200))

        text_content = "The completed lines disappear and grant the player points, and the player can proceed to fill the vacated spaces."
        text = text_font.render(text_content, True, self._colors["White"])
        rect = text.get_rect()
        self._screen.blit(text, ((self._width - rect[2])//2, 300))

        text_content = "The game ends when the playing field is filled."
        text = text_font.render(text_content, True, self._colors["White"])
        rect = text.get_rect()
        self._screen.blit(text, ((self._width - rect[2])//2, 400))

        text_content = "Reference: Wikipedia (2021), https://en.wikipedia.org/wiki/Tetris"
        text = text_font.render(text_content, True, self._colors["White"])
        self._screen.blit(text, (650, 600))

        text_content = "Press 'R' to return"
        text = text_font.render(text_content, True, self._colors["Red"])
        self._screen.blit(text, (30, 600))

        pygame.display.flip()
