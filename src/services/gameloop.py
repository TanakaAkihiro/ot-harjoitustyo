import sys
from entities.block import Block


class Gameloop:
    '''
    Luokka yhdelle pelikierrokselle.
    '''

    def __init__(self, event_queue, event_handler, clock, renderer, field, block_setter):
        self._field = field
        self._event_queue = event_queue
        self._event_handler = event_handler
        self._clock = clock
        self._renderer = renderer
        self._block_setter = block_setter

        self._block = None
        self._emptied_rows = 0

    def start(self):
        '''
        Aloittaa pelkierroksen.
        '''

        self._renderer.show_screen()
        new_block = True
        while True:
            if self._field.check_filled_rows():
                self._emptied_rows += self._field.empty_filled_rows()
            else:
                current_field = self._field.get_field()
                if current_field[0][4] == 1 or current_field[0][5] == 1:
                    return self._emptied_rows

                if new_block:
                    self._block = self._block_setter.set_new_block()
                    new_block = False

                event = self._event_handler.handle_events(self._event_queue, self._renderer, self._field, self._block, self._emptied_rows)

                if event:
                    self._block = None
                    new_block = True
                elif event is False:
                    sys.exit()

            self._renderer.draw_field(
                self._field.get_field(), self._block, self._emptied_rows)

            self._clock.tick(7)
