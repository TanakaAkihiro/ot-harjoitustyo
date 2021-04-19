import pygame

class Field:
    def __init__(self, field):
        self._field = field

    def get_field(self):
        return self._field
    
    def update(self, new_field):
        self._field = new_field
    
    def check_filled_rows(self):
        for i in self._field:
            