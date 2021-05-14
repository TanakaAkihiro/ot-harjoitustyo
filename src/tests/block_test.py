import unittest
from entities.block import Block


class TestBlock(unittest.TestCase):
    def setUp(self):
        self.block = Block()
        self.block._block_type = 0
        self.block.shape = self.block._shapes[self.block._block_type][0]
        self.field = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        self.block.move()

    def test_block_is_appearing_on_the_field(self):
        self.assertEqual((self.block.row, self.block.column), (0, 4))

    def test_block_is_falling(self):
        self.block.move()
        self.assertEqual((self.block.row, self.block.column), (1, 4))

    def test_check_if_the_block_is_able_to_fall(self):
        result = self.block.movable(self.field)
        self.assertTrue(result)
        self.field = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 0, 0, 0, 0]
        ]
        result = self.block.movable(self.field)
        self.assertFalse(result)

    def test_move_the_block_to_left(self):
        self.block.move((0, -1))
        self.assertEqual((self.block.row, self.block.column), (0, 3))

    def test_move_the_block_to_right(self):
        self.block.move((0, 1))
        self.assertEqual((self.block.row, self.block.column), (0, 5))

    def test_check_if_the_block_is_movable_to_left(self):
        result = self.block.movable(self.field, (0, -1))
        self.assertTrue(result)

        self.block.move((0, -1))
        self.block.move((0, -1))
        self.block.move((0, -1))
        result = self.block.movable(self.field, (0, -1))
        self.assertFalse(result)

        self.field = [
            [1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 0, 0, 0, 0, 0]
        ]
        result = self.block.movable(self.field, (0, -1))
        self.assertFalse(result)

    def test_check_if_the_block_is_movable_to_right(self):
        result = self.block.movable(self.field, (0, 1))
        self.assertTrue(result)

        self.block.move((0, 1))
        self.block.move((0, 1))
        self.block.move((0, 1))
        result = self.block.movable(self.field, (0, 1))
        self.assertFalse(result)

        self.field = [
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1]
        ]
        result = self.block.movable(self.field, (0, 1))
        self.assertFalse(result)

    def test_stop_the_block_on_the_bottom(self):
        self.block.move()
        self.block.move()
        self.block.move()
        
        result = self.block.movable(self.field)
        self.assertFalse(result)

        result = self.block.stop(self.field)
        self.assertEqual(result, [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 1, 0, 0, 0]
        ])

    def test_rotate_the_block_clockwise(self):
        self.block.rotate(1)
        self.assertEqual(self.block.shape, [[-1, 0], [0, 0], [1, 0], [2, 0]])

    def test_rotate_the_block_clockwise_when_block_orientation_is_3(self):
        self.block._block_orientation = 3
        self.shape = self.block._shapes[self.block._block_type][self.block._block_orientation]
        self.block.rotate(1)
        self.assertEqual(self.block.shape, [[0, -1], [0, 0], [0, 1], [0, 2]])

    def test_rotate_the_block_anti_clockwise(self):
        self.block.rotate(-1)
        self.assertEqual(self.block.shape, [[0, 0], [1, 0], [2, 0], [3, 0]])

    def test_rotate_the_block_anti_clockwise_when_block_orientation_is_1(self):
        self.block._block_orientation = 1
        self.shape = self.block._shapes[self.block._block_type][self.block._block_orientation]
        self.block.rotate(-1)
        self.assertEqual(self.block.shape, [[0, -1], [0, 0], [0, 1], [0, 2]])

    def test_return_false_when_check_if_the_block_is_rotatable_and_block_is_O_type(self):
        self.block._block_type = 1
        result = self.block.rotatable(self.field, 1)
        self.assertFalse(result)

    def test_return_true_when_check_if_the_block_is_rotatable_clockwise(self):
        result = self.block.rotatable(self.field, 1)
        self.assertTrue(result)

    def test_return_false_when_check_if_the_block_is_rotatable_clockwise(self):
        self.field = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 1, 0, 0, 0]
        ]
        result = self.block.rotatable(self.field, 1)
        self.assertFalse(result)

    def test_return_true_when_check_if_the_block_is_rotatable_clockwise_and_block_orientation_is_3(self):
        self.block._block_orientation = 3
        self.shape = self.block._shapes[self.block._block_type][self.block._block_orientation]
        result = self.block.rotatable(self.field, 1)
        self.assertTrue(result)

    def test_return_false_when_check_if_the_block_is_rotatable_clockwise_and_block_orientation_is_3(self):
        self.block._block_orientation = 3
        self.shape = self.block._shapes[self.block._block_type][self.block._block_orientation]
        self.field = [
            [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 1, 0, 0, 0]
        ]
        result = self.block.rotatable(self.field, 1)
        self.assertFalse(result)

    def test_return_true_when_check_if_the_block_is_rotatable_anti_clockwise(self):
        result = self.block.rotatable(self.field, -1)
        self.assertTrue(result)

    def test_return_false_when_check_if_the_block_is_rotatable_anti_clockwise(self):
        self.field = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 1, 0, 0, 0]
        ]
        result = self.block.rotatable(self.field, -1)
        self.assertFalse(result)

    def test_true_when_game_is_over_and_false_when_not(self):
        result = self.block.check_game_over(self.field)
        self.assertFalse(result)


        self.field = [
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 1, 0, 0, 0]
        ]
        result = self.block.check_game_over(self.field)
        self.assertTrue(result)

    
