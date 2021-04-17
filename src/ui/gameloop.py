import pygame
from entities.block import Block


class Gameloop:
    def __init__(self, screen, height, width, coefficient, event_queue, clock, renderer, field):
        self._screen = screen
        self._height = height
        self._width = width
        self._coefficient = coefficient
        self._new_block = True
        self._event_queue = event_queue
        self._clock = clock
        self._renderer = renderer

        self._field = field
    
    def start(self):
        self._renderer.show_screen()
        while True:
            for event in self._event_queue.get():
                if event.type == pygame.QUIT:
                    exit()

            if self._new_block:
                block = Block()
                self._new_block = False
            
            if not block.movable(self._field):
                self._new_block = True
                self._field = block.stop(self._field)
            elif block.movable(self._field) == "gameover":
                break
            else:
                self._field = block.move(self._field)
            
            self._renderer.draw_field(self._field)

            self._clock.tick(10)
            

    def show_screen(self, screen):
        screen.fill((255,255,255))

        for r in range(self._height):
            for c in range(self._width):
                pygame.draw.rect(screen, (0,0,0), (220 + self._coefficient*c, 100 + self._coefficient*r, self._coefficient, self._coefficient),1)

        pygame.display.flip()
    
    def draw_field(self, field, screen):
        for r in range(self._height):
            for c in range(self._width):
                pygame.draw.rect(screen, (192,192,192), (221 + self._coefficient*c, 101 + self._coefficient*r, self._coefficient-1, self._coefficient-1))
                if field[c][r] == 1:
                    pygame.draw.rect(screen, (0,0,128), (221 + self._coefficient*c, 101 + self._coefficient*r, self._coefficient-1, self._coefficient-1))
                if field[c][r] == 2:
                    pygame.draw.rect(screen, (200,0,0), (221 + self._coefficient*c, 101 + self._coefficient*r, self._coefficient-1, self._coefficient-1))
        pygame.display.flip()