import pygame
from entities.block import Block


class Gameloop:
    '''
    Luokka yhdelle pelikierrokselle.
    '''

    def __init__(self, event_queue, clock, renderer, field):
        self._field = field
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

                event = self._handle_events()

                if event is None:
                    if not self._block.movable(self._field.get_field()):
                        new_block = True
                        self._field.update(
                            self._block.stop(self._field.get_field()))
                        self._block = None
                        continue
                    elif self._block.movable(self._field.get_field()) == "gameover":
                        break
                    else:
                        self._block.move()
                elif event is False:
                    exit()

            self._renderer.draw_field(self._field.get_field(), self._block)

            self._clock.tick(5)

    def _handle_events(self):
        '''
        Käsittelee näppäimistön tapahtumat
        '''

        event = self._event_queue.get()
        boolean = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if self._block.movable(self._field.get_field(), (0, -1)):
                    self._block.move((0, -1))
                    boolean = True
            if event.key == pygame.K_RIGHT:
                if self._block.movable(self._field.get_field(), (0, 1)):
                    self._block.move((0, 1))
                    boolean = True
            if event.key == pygame.K_DOWN:
                if self._block.movable(self._field.get_field(), (1, 0)):
                    self._block.move((1, 0))
            if event.key == pygame.K_UP:
                if self._block.rotatable(self._field.get_field(), 1):
                    self._block.rotate(1)
            if event.key == pygame.K_z:
                if self._block.rotatable(self._field.get_field(), -1):
                    self._block.rotate(-1)

            self._renderer.draw_field(self._field.get_field(), self._block)
            self._event_queue.clear_queue()
            if boolean:
                return True
            else:
                return

        elif event.type == pygame.QUIT:
            return False
