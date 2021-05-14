from random import randint


class Block:
    '''Luokka, joka käsittelee laskeutuvaa palikkaa

    Attributes:
        shapes: Taulukko kaikille palikoille ja sen asennoille
        block_type: Satunnainen kokonaisluku, joka määrää palikan muodon
        block_orientation: Kokonaiasluku, joka määrää palikan asennon
        shape: Taulukko laskeutuvan palikan tyypistä & asennoista
        row: Palikan sijainnin rivin indeksi
        column: Palikan sijainnin sarakkeen indeksi
    '''

    def __init__(self):
        '''Luokan konstruktori Block-oliolle
        '''
        self._shapes = [
            [  # I
                [[0, -1], [0, 0], [0, 1], [0, 2]],
                [[-1, 0], [0, 0], [1, 0], [2, 0]],
                [[0, -2], [0, -1], [0, 0], [0, 1]],
                [[0, 0], [1, 0], [2, 0], [3, 0]]

            ],
            [  # O
                [[1, 0], [0, 1], [0, 0], [1, 1]]
            ],
            [  # J
                [[0, -1], [1, -1], [1, 0], [1, 1]],
                [[0, 1], [0, 0], [1, 0], [2, 0]],
                [[2, 1], [1, -1], [1, 0], [1, 1]],
                [[2, -1], [0, 0], [1, 0], [2, 0]]
            ],
            [  # L
                [[0, 1], [1, -1], [1, 0], [1, 1]],
                [[2, 1], [0, 0], [1, 0], [2, 0]],
                [[2, -1], [1, -1], [1, 0], [1, 1]],
                [[0, -1], [0, 0], [1, 0], [2, 0]]
            ],
            [  # T
                [[0, 0], [1, -1], [1, 0], [1, 1]],
                [[1, 1], [0, 0], [1, 0], [2, 0]],
                [[2, 0], [1, -1], [1, 0], [1, 1]],
                [[1, -1], [0, 0], [1, 0], [2, 0]]
            ],
            [  # Z
                [[0, -1], [0, 0], [1, 0], [1, 1]],
                [[0, 1], [1, 1], [1, 0], [2, 0]],
                [[1, -1], [1, 0], [2, 0], [2, 1]],
                [[0, 0], [1, 0], [1, -1], [2, -1]]
            ],
            [  # S
                [[0, 0], [0, 1], [1, -1], [1, 0]],
                [[0, 0], [1, 0], [1, 1], [2, 1]],
                [[1, 1], [1, 0], [2, 0], [2, -1]],
                [[0, -1], [1, -1], [1, 0], [2, 0]]
            ]
        ]
        self._block_type = randint(0, len(self._shapes) - 1)
        self._block_orientation = 0
        self.shape = self._shapes[self._block_type][self._block_orientation]
        self.row = -1
        self.column = 4

    def move(self, direction=None):
        '''Liikuttaa palikan määrättyyn suuntaan. Jos suuntaa ei ole määritelty, palikka tippuu yhen ruudun verran alaspäin.

        Args:
            direction: Määrittää laskeutuvan palikan suunnan, mihin liikkuu.
        '''

        if direction is None:
            self.row += 1

        else:
            self.row += direction[0]
            self.column += direction[1]

    def movable(self, field, direction=None):
        '''Tarkistaa, onko palikkaa mahdollista liikuttaa parametrilla annettuun suuntaan. Jos suuntaa ei ole määritelty, suuntana oletetaan yhden rivin verran alempaa suuntaa.

        Args:
            field: Field-olio
            direction: Määrittää laskeutuvan palikan suunnan, mihin liikkuu.

        Returns:
            True, jos palikalla ei ole esteitä määrätyssä suunnassa.
            False muulloin.
        '''

        if direction is None:
            for i in self.shape:
                next_block = self.row + i[0] + 1
                if next_block > len(field) - 1:
                    return False
                if field[self.row+i[0]+1][self.column+i[1]] == 1:
                    return False
        else:
            for i in self.shape:
                next_block = (
                    self.row + i[0] + direction[0], self.column + i[1] + direction[1])
                condition_1 = next_block[0] > len(field) - 1
                condition_2 = next_block[1] > len(field[0]) - 1
                condition_3 = next_block[1] < 0
                if condition_1 or condition_2 or condition_3:
                    return False
                if field[next_block[0]][next_block[1]] == 1:
                    return False
        return True

    def stop(self, field):
        '''Tallentaa laskeutuneen palikan indeksit ruudukolle

        Args:
            field: Ruudukko taulukkona

        Returns:
            Uuden ruudukon taulukkona
        '''
        for i in self.shape:
            field[self.row + i[0]][self.column + i[1]] = 1
        return field

    def rotate(self, direction):
        '''Muuttaa palikan asentoa.

        Args:
            direction: Suunta, mihin päin pelaaja haluaa kääntää palikan
        '''
        if direction == 1:
            if self._block_orientation == 3:
                self.shape = self._shapes[self._block_type][0]
                self._block_orientation = 0
            else:
                self._block_orientation += direction
                self.shape = self._shapes[self._block_type][self._block_orientation]
        else:
            if self._block_orientation == 0:
                self.shape = self._shapes[self._block_type][3]
                self._block_orientation = 3
            else:
                self._block_orientation += direction
                self.shape = self._shapes[self._block_type][self._block_orientation]

    def rotatable(self, field, direction):
        '''Tarkistaa, onko mahdollista kääntää palikan asentoa määrättyyn suuntaan.

        Args:
            field: Ruudukko taulukkona
            direction: Suunta, mihinpäin pelaaja haluaa kääntää palikan

        Returns:
            True, jos kääntäminen on mahdollista
            False muulloin
        '''
        if self._block_type == 1:
            return False
        if direction == 1:
            if self._block_orientation == 3:
                for i in self._shapes[self._block_type][0]:
                    condition_1 = self.row + i[0] > len(field) - 1
                    condition_2 = self.column + i[1] > len(field[0]) - 1
                    condition_3 = self.column + i[1] < 0
                    if condition_1 or condition_2 or condition_3:
                        return False
                    condition_4 = field[self.row +
                                        i[0]][self.column + i[1]] == 1
                    if condition_4:
                        return False
            else:
                for i in self._shapes[self._block_type][self._block_orientation + direction]:
                    condition_1 = self.row + i[0] > len(field) - 1
                    condition_2 = self.column + i[1] > len(field[0]) - 1
                    condition_3 = self.column + i[1] < 0
                    if condition_1 or condition_2 or condition_3:
                        return False
                    condition_4 = field[self.row +
                                        i[0]][self.column + i[1]] == 1
                    if condition_4:
                        return False
        else:
            for i in self._shapes[self._block_type][self._block_orientation + direction]:
                condition_1 = self.row + i[0] > len(field) - 1
                condition_2 = self.column + i[1] > len(field[0]) - 1
                condition_3 = self.column + i[1] < 0
                if condition_1 or condition_2 or condition_3:
                    return False
                condition_4 = field[self.row +
                                    i[0]][self.column + i[1]] == 1
                if condition_4:
                    return False
        return True

    def check_game_over(self, field):
        '''Tarkistaa, loppuuko pelikierros

        Args:
            field: Tämänhetkinen ruudukko taulukkona

        Returns:
            True, jos uudelle palikalle ei ole tilaa eli pelikierros päättyy
            False muuten
        '''
        for i in self.shape:
            if field[self.row + i[0] + 1][self.column + i[1]] == 1:
                return True
        return False
