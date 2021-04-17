import pygame

class Renderer:
    def __init__(self, screen, height, width, coefficient):
        self._screen = screen
        self._height = height
        self._width = width
        self._coefficient = coefficient
    
    def show_screen(self):
        self._screen.fill((255,255,255))

        for r in range(self._height):
            for c in range(self._width):
                pygame.draw.rect(self._screen, (0,0,0), (220 + self._coefficient*c, 100 + self._coefficient*r, self._coefficient, self._coefficient),1)

        pygame.display.flip()
    
    def draw_field(self, field):
        for r in range(self._height):
            for c in range(self._width):
                pygame.draw.rect(self._screen, (192,192,192), (221 + self._coefficient*c, 101 + self._coefficient*r, self._coefficient-1, self._coefficient-1))
                if field[c][r] == 1:
                    pygame.draw.rect(self._screen, (0,0,128), (221 + self._coefficient*c, 101 + self._coefficient*r, self._coefficient-1, self._coefficient-1))
                if field[c][r] == 2:
                    pygame.draw.rect(self._screen, (200,0,0), (221 + self._coefficient*c, 101 + self._coefficient*r, self._coefficient-1, self._coefficient-1))
        pygame.display.flip()