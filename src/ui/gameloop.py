import pygame
from entities.block import Block


class Gameloop:
    def __init__(self, screen, height, width, coefficient, event_queue, clock, renderer, field):
        self._screen = screen
        self._height = height
        self._width = width
        self._coefficient = coefficient
        self._event_queue = event_queue
        self._clock = clock
        self._renderer = renderer
        self._field = field

        self._new_block = True
    
    def start(self):
        self._renderer.show_screen()
        while True:
            if self._handle_events() == False:
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
    
    def _handle_events(self):
        for event in self._event_queue.get():
            if event.type == pygame.QUIT:
                return False