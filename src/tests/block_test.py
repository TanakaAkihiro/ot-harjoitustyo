import unittest
from entities.block import Block

class TestBlock(unittest.TestCase):
    def setUp(self):
        self.block = Block()
        self.block.shape = self.block.shapes[0]
        self.field = [
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0]
        ]
    
    def test_block_is_appearing_on_the_field(self):
        result = self.block.move(self.field)
        self.assertEqual(result, [
            [0,0,0,1,1,1,1,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0]
        ])
    
    def test_block_is_falling(self):
        self.field = self.block.move(self.field)
        result = self.block.move(self.field)
        self.assertEqual(result, [
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,1,1,1,1,0,0,0],
            [0,0,0,0,0,0,0,0,0,0]
        ])
    
    def test_block_can_be_moved_to_left(self):
        self.field = [
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,1,1,1,1,0,0,0],
            [0,0,0,0,0,0,0,0,0,0]
        ]
        result = self.block.move(self.field, (0,-1))
        self.assertEqual(result, [
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,1,1,1,1,0,0,0],
            [0,0,1,1,1,1,0,0,0,0]
        ])
    
    def test_blovk_can_be_moved_to_right(self):
        self.field = [
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,1,1,1,1,0,0,0],
            [0,0,0,0,0,0,0,0,0,0]
        ]
        result = self.block.move(self.field, (0,1))
        self.assertEqual(result, [
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,1,1,1,1,0,0,0],
            [0,0,0,0,1,1,1,1,0,0]
        ])