import unittest
import pygame
from services.gameloop import Gameloop


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
        if self.events == []:
            return None
        return self.events[0]

    def get_all(self):
        return self.events

    def clear_queue(self):
        pass


class StubEventHandler:
    def handle_game_events(self, event_queue, renderer, field, block, emptied_rows):
        if not block.movable(field):
            field.update(block.stop(field.get_field()))
            return True
        else:
            block.move()
        if event_queue.get() is not None:
            if event_queue.get().type == pygame.QUIT:
                return False


class StubRenderer:
    def show_game_background(self):
        pass

    def draw_field(self, field, block, emptied_rows):
        pass

    def save_new_score(self, emptied_rows):
        return "Player"


class StubBlock:
    def __init__(self):
        self.shape = [
            [0, 1], [0, 0], [0, 1], [0, 2]
        ]
        self.row = -1
        self.column = 4

    def movable(self, field):
        for i in self.shape:
            if field.get_field()[self.row + 1][self.column + i[1]] == 1:
                return False
        return True

    def move(self):
        self.row += 1

    def stop(self, field):
        for i in self.shape:
            field[self.row + i[0]][self.column + i[1]] = 1
        return field

    def check_game_over(self, field):
        for i in self.shape:
            if field[self.row + i[0] + 1][self.column + i[1]] == 1:
                return True
        return False


class StubBlockSetter:
    def set_new_block(self):
        return StubBlock()


class StubField:
    def __init__(self, field):
        self.field = field
        self.x = 0

    def get_field(self):
        return self.field

    def update(self, new_field):
        self.field = new_field

    def empty_filled_rows(self):
        return 1

    def check_filled_rows(self):
        if self.x == 0:
            self.x = 1
            return True
        return False


class TestGameloop(unittest.TestCase):
    def test_return_emptied_rows_when_game_is_over(self):
        field = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        ]

        gameloop = Gameloop(
            StubEventQueue([]),
            StubEventHandler(),
            StubClock(),
            StubRenderer(),
            StubField(field),
            StubBlockSetter()
        )

        result = gameloop.start()
        self.assertEqual(result, ("Player", 1))
