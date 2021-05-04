import unittest
from services.gameloop import Gameloop
from entities.field import Field

class StubClock:
    def tick(self, fps):
        pass

class StubEvent:
    def __init__(self, event_type, key):
        self.type = event_type
        self.key = key
    
class StubEventQueue:
    def __init__(self, events):
        self.events = events

    def get(self):
        return self.events[0]
    
    def get_all(self):
        return self.events
    
    def clear_queue(self):
        self.events = []

class StubEventHandler:
    def handle_events(self, event_queue, renderer, field, block, emptied_rows, current_field):
        if not block.movable(field):
            return True
        if event_queue.get().type == pygame.QUIT:
            return False

class StubRenderer:
    def show_screen(self):
        pass

    def draw_field(self, field, block, emptied_rows):
        pass

class StubBlock:
    def movable(field):
        for i in field.get_field():
            if i != [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]:
                return False

class StubBlockSetter:
    def set_new_block(self):
        return StubBlock()

class TestGameloop(unittest.TestCase):
    def test_can_exit_from_the_application(self):
        events = [
            StubEvent(pygame.QUIT, None)
        ]
        
        field = [
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
        ]

        gameloop = Gameloop(
            StubEventQueue(events),
            StubEventHandler(),
            StubClock(),
            StubRenderer(),
            Field(field),
            StubBlockSetter()            
        )

        gameloop.start()

        