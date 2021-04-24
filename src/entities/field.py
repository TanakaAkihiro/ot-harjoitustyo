class Field:

    '''
    Luokka ruudukon käsittelyyn.
    ...

    Attribuutti
    -----------
    field: list
        taulukko tetriksen ruudukosta
    '''

    def __init__(self, field):
        self._field = field

    def get_field(self):
        '''
        Palauttaa ruudukon.
        '''
        return self._field

    def update(self, new_field):
        '''
        Päivittää ruudukon.
        '''

        self._field = new_field

    def empty_filled_rows(self):
        '''
        Tyhjentää täytetyt rivit.
        '''

        index = 0
        for row in self._field:
            if row == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]:
                self._field = self._field[:index] + self._field[index + 1:]
                self._field = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]] + self._field
            index += 1

    def check_filled_rows(self):
        '''
        Palauttaa True, jos ruudukossa on täytetty rivi.
        '''

        for row in self._field:
            if row == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]:
                return True
        return False
