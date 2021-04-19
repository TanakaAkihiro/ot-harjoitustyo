import unittest
from entities.field import Field

class TestField(unittest.TestCase):
    def setUp(self):
        field = [
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0]
        ]
        self.field = Field(field)
    
    def test_get_the_current_field(self):
        result = self.field.get_field()
        self.assertEqual(result, [
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0]
        ])
    
    def test_update_the_field_correctly(self):
        self.field.update([
            [1,1,1,1,1,1,1,1,1,1],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0]
        ])
        self.assertEqual(self.field.get_field(), [
            [1,1,1,1,1,1,1,1,1,1],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0]
        ])
    
    def test_empty_correctly_filled_rows(self):
        self.field.update([
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [2,2,2,2,2,2,2,2,2,2]
        ])
        self.field.empty_filled_rows()
        self.assertEqual(self.field.get_field(), [
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0]
        ])