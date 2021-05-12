import pygame


class RankingView:
    def __init__(self, screen, height, width, coefficient, cell_size, score_repository):
        self._screen = screen
        self._height = height
        self._width = width
        self._coefficient = coefficient
        self._cell_size = cell_size
        self._score_repository = score_repository

        self._colors = {"White": (255, 255, 255), "Black": (0, 0, 0), "Grey": (
            192, 192, 192), "Blue": (0, 0, 128), "Red": (200, 0, 0)}
    
    def render(self):
        self._screen.fill(self._colors["Black"])

        text_font = pygame.font.SysFont(None, 48)
        text_content = "TOP 10"
        text = text_font.render(text_content, True, self._colors["White"])
        rect = text.get_rect()
        self._screen.blit(text, (((self._height*self._cell_size) - rect[3])//2, 50))

        text_content = self._score_repository.find_ranking()
        text = text_font.render(str(text_content), True, self._colors["White"])
        self._screen.blit(text, (0, 300))
        pygame.display.flip()