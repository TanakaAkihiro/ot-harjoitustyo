from random import randint


class Block:
    '''
    Luokka palikoiden käsittelyyn
    ...

    Attribuutit
    -----------
    shapes: list
        Taulukko kaikille palikoille ja sen asennoille
    index: int
        Satunnainen kokonaisluku, jonka avulla määritetään yksi palikkatyyppi taulukosta shapes
    shape: list
        Taulukko satunnaisesti valitun palikan asetelmasta ja asennosta
    row: int
        Palikan sijainnin rivi-indeksi
    column: int
        Palikan sijainnin sarakeindeksi
    '''

    def __init__(self):
        self._shapes = [
            [ # I
                [[0, -1], [0, 0], [0, 1], [0, 2]],
                [[-1, 0], [0, 0], [1, 0], [2, 0]],
                [[0, -2], [0, -1], [0, 0], [0, 1]],
                [[0, 0], [1, 0], [2, 0], [3, 0]]

            ],
            [ # O
                [[1, 0], [0, 1], [0, 0], [1, 1]]
            ],
            [ # J
                [[0, -1], [1, -1], [1, 0], [1, 1]],
                [[0, 1], [0, 0], [1, 0], [2, 0]],
                [[2, 1], [1, -1], [1, 0], [1, 1]],
                [[2, -1], [0, 0], [1, 0], [2, 0]]
            ],
            [ # L
                [[0, 1], [1, -1], [1, 0], [1, 1]],
                [[2, 1], [0, 0], [1, 0], [2, 0]],
                [[2, -1], [1, -1], [1, 0], [1, 1]],
                [[0, -1], [0, 0], [1, 0], [2, 0]]
            ],
            [ # T
                [[0, 0], [1, -1], [1, 0], [1, 1]],
                [[1, 1], [0, 0], [1, 0], [2, 0]],
                [[2, 0], [1, -1], [1, 0], [1, 1]],
                [[1, -1], [0, 0], [1, 0], [2, 0]]
            ],
            [ # Z
                [[0, -1], [0, 0], [1, 0], [1, 1]],
                [[0, 1], [1, 1], [1, 0], [2, 0]],
                [[1, -1], [1, 0], [2, 0], [2, 1]],
                [[0, 0], [1, 0], [1, -1], [2, -1]]
            ],
            [ # S
                [[0, 0], [0, 1], [1, -1], [1, 0]],
                [[0, 0], [1, 0], [1, 1], [2, 1]],
                [[1, 1], [1, 0], [2, 0], [2, -1]],
                [[0, -1], [1, -1], [1, 0], [2, 0]]
            ]
        ]
        self._block_type = randint(0, len(self._shapes) - 1)
        self._block_rotation = 0
        self.shape = self._shapes[self._block_type][self._block_rotation]
        self.row = -1
        self.column = 4

    def move(self, field, direction=None):
        '''
        Palauttaa ruudukon, jossa palikka on liikutettu haluttuun suuntaan.
        Jos suuntaa ei ole määritelty, palikka liikkuu yhen rivin verran alaspäin.
        '''

        if direction is None:
            self.row += 1

        else:
            self.row += direction[0]
            self.column += direction[1]
        return field

    def movable(self, field, direction=None):
        '''
        Tarkistaa, onko palikkaa mahdollista liikuttaa parametrilla annettuun suuntaan
        ja palauttaa totuusarvon.
        Jos suuntaa ei ole määritelty, suuntana oletetaan yhden rivin verran alempaa suuntaa.
        '''

        if direction is None:
            for i in self.shape:
                next_block = self.row + i[0] + 1
                if next_block > len(field) - 1:
                    return False
                if next_block < 0:
                    return "gameover"
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
        '''
        Palauttaa ruudukon, jossa palikka pysäytetään liikkumasta.
        '''
        for i in self.shape:
            field[self.row + i[0]][self.column + i[1]] = 1
        return field

    def rotate(self, direction):
        '''
        Muuta palikan asento.
        '''
        if self._block_type == 1:  #Jos palikka on O-tyyppinen, palautetaan None
            return
        if direction == 1:
            if self._block_rotation == 3:
                self.shape = self._shapes[self._block_type][0]
                self._block_rotation = 0
            else:
                self._block_rotation += direction
                self.shape = self._shapes[self._block_type][self._block_rotation]
        else:
            if self._block_rotation == 0:
                self.shape = self._shapes[self._block_type][3]
                self._block_rotation = 3
            else:
                self._block_rotation += direction
                self.shape = self._shapes[self._block_type][self._block_rotation]
                
    def rotatable(self, field, direction):
        '''
        Tarkista, onko mahdollista muuttaa palikan asentoa haluttuun suuntaan.
        '''
        if self._block_type == 1:
            return False
        if direction == 1:
            if self._block_rotation == 3:
                for i in self._shapes[self._block_type][0]:
                    condition_1 = self.row + i[0] > len(field) - 1
                    condition_2 = self.column + i[1] > len(field[0]) - 1
                    condition_3 = self.column + i[1] < 0
                    condition_4 = field[self.row + i[0]][self.column + i[1]] == 1
                    if condition_1 or condition_2 or condition_3 or condition_4:
                        return False
            else:
                for i in self._shapes[self._block_type][self._block_rotation + direction]:
                    condition_1 = self.row + i[0] > len(field) - 1
                    condition_2 = self.column + i[1] > len(field[0]) - 1
                    condition_3 = self.column + i[1] < 0
                    condition_4 = field[self.row + i[0]][self.column + i[1]] == 1
                    if condition_1 or condition_2 or condition_3 or condition_4:
                        return False
        else:
            if self._block_rotation == 0:
                for i in self._shapes[self._block_type][3]:
                    condition_1 = self.row + i[0] > len(field) - 1
                    condition_2 = self.column + i[1] > len(field[0]) - 1
                    condition_3 = self.column + i[1] < 0
                    condition_4 = field[self.row + i[0]][self.column + i[1]] == 1
                    if condition_1 or condition_2 or condition_3 or condition_4:
                        return False
            else:
                for i in self._shapes[self._block_type][self._block_rotation + direction]:
                    condition_1 = self.row + i[0] > len(field) - 1
                    condition_2 = self.column + i[1] > len(field[0]) - 1
                    condition_3 = self.column + i[1] < 0
                    condition_4 = field[self.row + i[0]][self.column + i[1]] == 1
                    if condition_1 or condition_2 or condition_3 or condition_4:
                        return False
        return True
