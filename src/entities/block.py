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
        self.shapes = [
            [[0, -1], [0, 0], [0, 1], [0, 2]],
            [[1, 0], [0, 1], [0, 0], [1, 1]],
            [[0, -1], [1, -1], [1, 0], [1, 1]],
            [[0, 1], [1, -1], [1, 0], [1, 1]],
            [[0, 0], [1, -1], [1, 0], [1, 1]],
            [[0, -1], [0, 0], [1, 0], [1, 1]],
            [[0, 0], [0, 1], [1, -1], [1, 0]]
        ]
        self._index = randint(0, len(self.shapes) - 1)
        self.shape = self.shapes[self._index]
        self.row = -1
        self.column = 4

    def move(self, field, direction=None):
        '''
        Palauttaa ruudukon, jossa palikka on liikutettu haluttuun suuntaan.
        Jos suuntaa ei ole määritelty, palikka liikkuu yhen rivin verran alaspäin.
        '''

        if direction is None:
            self.row += 1
            for i in self.shape:
                field[self.row + i[0]][self.column + i[1]] = 1
            if self.row != 0:
                for i in self.shape:
                    if i[0] == 0:
                        field[self.row + i[0] - 1][self.column + i[1]] = 0
                    elif i[0] != 0 and [i[0] - 1, i[1]] not in self.shape:
                        field[self.row + i[0] - 1][self.column + i[1]] = 0

        else:
            if direction[1] != 1:
                for i in self.shape:
                    field[self.row + i[0] + direction[0]
                          ][self.column + i[1] + direction[1]] = 1
                    neighbor_r = self.row + i[0] - direction[0]
                    neighbor_c = self.column + i[1] - direction[1]
                    try:
                        if direction[1] == -1 and field[neighbor_r][neighbor_c] in (0, 2):
                            field[self.row + i[0]][self.column + i[1]] = 0
                        elif direction[0] == 1 and field[neighbor_r][neighbor_c] in (0, 2):
                            field[self.row + i[0]][self.column + i[1]] = 0
                    except IndexError:
                        field[self.row + i[0]][self.column + i[1]] = 0
            else:
                for i in range(len(self.shape)-1, -1, -1):
                    field[self.row + self.shape[i][0] + direction[0]
                          ][self.column + self.shape[i][1] + direction[1]] = 1
                    neighbor_r = self.row + self.shape[i][0] - direction[0]
                    neighbor_c = self.column + self.shape[i][1] - direction[1]
                    if field[neighbor_r][neighbor_c] in (0, 2):
                        field[self.row + self.shape[i][0]
                              ][self.column + self.shape[i][1]] = 0
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
                elif next_block < 0:
                    return "gameover"
                elif field[self.row+i[0]+1][self.column+i[1]] == 2:
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
                elif field[next_block[0]][next_block[1]] == 2:
                    return False
        return True

    def stop(self, field):
        '''
        Palauttaa ruudukon, jossa palikka pysäytetään liikkumasta.
        '''

        for i in self.shape:
            field[self.row + i[0]][self.column + i[1]] = 2
        return field
