class Field:
    def __init__(self, field):
        self._field = field

    def get_field(self):
        return self._field

    def update(self, new_field):
        self._field = new_field

    def empty_filled_rows(self):
        index = 0
        for row in self._field:
            if row == [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]:
                self._field = self._field[:index] + self._field[index + 1:]
                self._field = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]] + self._field
            index += 1
