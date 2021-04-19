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
        self._block = None
        
    
    def start(self):
        self._renderer.show_screen()
        while True:
            if self._new_block:
                self._block = Block()
                self._new_block = False
            
            if self._handle_events() == False:
                exit()
            
            else:
                if not self._block.movable(self._field.get_field()):
                    self._new_block = True
                    self._field.update(self._block.stop(self._field.get_field()))
                    self._block = None
                    continue
                elif self._block.movable(self._field.get_field()) == "gameover":
                    break
                else:
                    self._field.update(self._block.move(self._field.get_field()))
            
            self._renderer.draw_field(self._field.get_field())

            self._clock.tick(10)
    
    def _handle_events(self):
        for event in self._event_queue.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if self._block.movable(self._field.get_field(), (0,-1)):
                        self._field.update(self._block.move(self._field.get_field(), (0,-1)))
                elif event.key == pygame.K_RIGHT:     
                    if self._block.movable(self._field.get_field(), (0,1)):
                        self._field.update(self._block.move(self._field.get_field(), (0,1)))
                elif event.key == pygame.K_DOWN:
                    if self._block.movable(self._field.get_field(), (1,0)):
                        self._field.update(self._block.move(self._field.get_field(), (1,0)))
            elif event.type == pygame.QUIT:
                return False