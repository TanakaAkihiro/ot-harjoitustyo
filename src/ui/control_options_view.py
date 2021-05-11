import pygame


class ControlOptionsView:
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
