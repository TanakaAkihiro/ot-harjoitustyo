class Field:
    '''Luokka ruudukon käsittelyyn.

    Attributes:
        field: Tetriksen ruudukko taulukkona
    '''

    def __init__(self, field):
        '''Luokan konstruktori, joka luo uuden ruudukon

        Args:
            field: Ruudukko taulukkona
        '''
        self._field = field

    def get_field(self):
        '''Palauttaa ruudukon

        Returns:
            Ruudukon taulukkona
        '''
        return self._field

    def update(self, new_field):
        '''Päivittää ruudukon.
        
        Args:
            new_field: Uusi ruudukko taulukkona
        '''

        self._field = new_field

    def empty_filled_rows(self):
        '''Tyhjentää täytetyt rivit
        
        Returns:
            Tyhjennettyjen rivien määrä
        '''

        count = 0
        index = 0
        for row in self._field:
            if row == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]:
                self._field = self._field[:index] + self._field[index + 1:]
                self._field = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]] + self._field
                count += 1
            index += 1
        return count

    def check_filled_rows(self):
        '''Etsii täytettyjä rivejä ruudukosta
        
        Returns:
            True, jos ruudukossa on täytetty rivi.
            False muulloin
        '''
        for row in self._field:
            if row == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]:
                return True
        return False
