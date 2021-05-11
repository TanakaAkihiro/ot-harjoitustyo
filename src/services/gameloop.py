import sys
from entities.block import Block


class Gameloop:
    '''Luokka yhdelle pelikierrokselle.

    Attributes:
        field: Field-olio
        event_queue: EventQueue-olio
        event_handler: EventHandler-olio
        clock: Clock-olio
        renderer: Renderer-olio
        block_setter: BlockSetter-olio
        block: Block-olio, palikka joka on laskeutumuassa
        emptied_rows: Tyhjennettyjen rivien määrä
    '''

    def __init__(self, event_queue, event_handler, clock, renderer, field, block_setter):
        '''Luokan konstruktori, joka alustaa tarvittavat luokat pelikierrosta varten

        Args:
            event_queue: EventQueue-olio
            event_handler: EventHandler-olio
            clock: Clock-olio
            renderer: Renderer-olio
            field: Field-olio
            block_setter: BlockSetter-olio
        '''
        self._field = field
        self._event_queue = event_queue
        self._event_handler = event_handler
        self._clock = clock
        self._renderer = renderer
        self._block_setter = block_setter

        self._block = None
        self._emptied_rows = 0

    def start(self):
        '''Aloittaa uuden pelkierroksen.
        '''

        self._renderer.show_game_background()
        new_block = True
        while True:
            if self._field.check_filled_rows():
                self._emptied_rows += self._field.empty_filled_rows()
            else:
                if new_block:
                    self._block = self._block_setter.set_new_block()
                    if self._block.check_game_over(self._field.get_field()):
                        return self._emptied_rows
                    new_block = False

                event = self._event_handler.handle_game_events(
                    self._event_queue, self._renderer, self._field, self._block, self._emptied_rows)

                if event:
                    self._block = None
                    new_block = True
                elif event is False:
                    sys.exit()

            self._renderer.draw_field(
                self._field.get_field(), self._block, self._emptied_rows)

            self._clock.tick(7)
