import pygame
from entities.block import Block


class Gameloop:
    '''
    Luokka yhdelle pelikierrokselle.
    '''

    def __init__(self, event_queue, clock, renderer, field):
        self._field = field
        self._height = len(self._field.get_field())
        self._width = len(self._field.get_field()[0])
        self._event_queue = event_queue
        self._clock = clock
        self._renderer = renderer

        self._block = None

    def start(self):
        '''
        Aloittaa pelkierroksen.
        '''

        self._renderer.show_screen()
        new_block = True
        while True:
            if self._field.check_filled_rows():
                self._field.empty_filled_rows()
            else:
                if new_block:
                    self._block = Block()
                    new_block = False

                if self._handle_events() is False:
                    exit()
                else:
                    if not self._block.movable(self._field.get_field()):
                        new_block = True
                        self._field.update(
                            self._block.stop(self._field.get_field()))
                        self._block = None
                        continue
                    elif self._block.movable(self._field.get_field()) == "gameover":
                        break
                    else:
                        self._field.update(
                            self._block.move(self._field.get_field()))

            self._renderer.draw_field(self._field.get_field())

            self._clock.tick(4)

    def _handle_events(self):
        '''
        Käsittelee näppäimistön tapahtumat
        '''

        for event in self._event_queue.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if self._block.movable(self._field.get_field(), (0, -1)):
                        self._field.update(self._block.move(
                            self._field.get_field(), (0, -1)))
                elif event.key == pygame.K_RIGHT:
                    if self._block.movable(self._field.get_field(), (0, 1)):
                        self._field.update(self._block.move(
                            self._field.get_field(), (0, 1)))
                elif event.key == pygame.K_DOWN:
                    if self._block.movable(self._field.get_field(), (1, 0)):
                        self._field.update(self._block.move(
                            self._field.get_field(), (1, 0)))
            elif event.type == pygame.QUIT:
                return False
