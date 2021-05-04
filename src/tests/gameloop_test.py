import unittest
import pygame
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
    def handle_events(self, event_queue, renderer, field, block, emptied_rows):
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
    def movable(self, field):
        for i in field.get_field():
            if i != [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]:
                return False


class StubBlockSetter:
    def set_new_block(self):
        return StubBlock()


class TestGameloop(unittest.TestCase):
    def test_game_ends_when_there_is_a_block_on_either_two_center_squares_in_the_top_row(self):
        field = [
            [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]

        gameloop = Gameloop(
            StubEventQueue([]),
            StubEventHandler(),
            StubClock(),
            StubRenderer(),
            Field(field),
            StubBlockSetter()
        )

        result = gameloop.start()
        self.assertEqual(result, 0)
