class Block:
    def __init__(self):
        self.shape = [[0, -1], [0,0], [0, 1], [0, 2]]
        self.row = -1
        self.column = 4
    
    def move(self, field, direction = None):
        if direction is None:
            self.row += 1
            for i in self.shape:
                field[self.row + i[0]][self.column + i[1]] = 1
            if self.row != 0:
                for i in self.shape:
                    field[self.row + i[0] - 1][self.column + i[1]] = 0
        else:
            for i in self.shape:
                field[self.row + i[0] + direction[0]][self.column + i[1] + direction[1]] = 1
                if field[self.row + i[0] - direction[0]][self.column + i[1] - direction[1]] == 0:
                    field[self.row + i[0]][self.column + i[1]] = 0
            self.row += direction[0]
            self.column += direction[1]
        return field

    def movable(self, field, direction = None):
        if direction is None:
            for i in self.shape:
                next_block = self.row + i[0] + 1
                if next_block > len(field) - 1:
                    return False
                elif next_block < 0:
                    return "gameover"
                elif field[self.row+i[0]+1][self.column+i[1]]!= 0:
                    return False
        else:
            for i in self.shape:
                next_block = (self.row + i[0] + direction[0], self.column + i[1] + direction[1])
                if next_block[0] > len(field) - 1 or next_block[1] > len(field[0]) - 1 or next_block[1] < 0:
                    return False
                elif field[next_block[0]][next_block[1]] == 2:
                    return False
        return True

    def stop(self, field):
        for i in self.shape:
            field[self.row + i[0]][self.column + i[1]] = 2
        return field