import pygame


class HighScoresView:
    def __init__(self, screen, width, height, score_repository):
        self._screen = screen
        self._width = width
        self._height = height
        self._score_repository = score_repository

        self._colors = {"White": (255, 255, 255), "Black": (0, 0, 0), "Grey": (
            192, 192, 192), "Blue": (0, 0, 128), "Red": (200, 0, 0)}

    def render(self):
        self._screen.fill(self._colors["Black"])

        text_font = pygame.font.SysFont(None, 48)
        text_content = "TOP 10"
        text = text_font.render(text_content, True, self._colors["White"])
        rect = text.get_rect()
        self._screen.blit(text, ((self._width - rect[2])//2, 50))

        text_font = pygame.font.SysFont(None, 36)
        high_scores = self._score_repository.find_high_scores()

        x = 0
        for i in range(10):
            if len(high_scores) - 1 >= i:
                text = text_font.render(str(high_scores[i][0]), True, self._colors["White"])
                self._screen.blit(text, ((self._width - rect[2]*2.5)//2, 150 + x))
                
                text = text_font.render(str(high_scores[i][1]), True, self._colors["White"])
                self._screen.blit(text, ((self._width + rect[2]*2)//2, 150 + x))
            else:
                text = text_font.render("Player", True, self._colors["White"])
                self._screen.blit(text, ((self._width - rect[2]*2.5)//2, 150 + x))
                
                text = text_font.render("0", True, self._colors["White"])
                self._screen.blit(text, ((self._width + rect[2]*2)//2, 150 + x))

            x += 50

        text_content = "Press 'R' to return"
        text = text_font.render(text_content, True, self._colors["Red"])
        self._screen.blit(text, (100, 600))

        text_content = "Press 'D' to reset high scores"
        text = text_font.render(text_content, True, self._colors["Red"])
        self._screen.blit(text, (1000, 600))

        pygame.display.flip()
