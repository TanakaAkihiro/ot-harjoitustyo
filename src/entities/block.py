class Block:
    def __init__(self):
        self.shape = [[-1, 0], [0,0], [1,0], [2,0]]
        self.row = -1
        self.column = 4
    
    def move(self, field):
        if self.movable(field):
            self.row += 1
            if self.row == 0:
                for i in self.shape:
                    field[self.column + i[0]][self.row + i[1]] = 1
            else:
                for i in self.shape:
                    field[self.column + i[0]][self.row + i[1]] = 1
                    field[self.column + i[0]][self.row + i[1] - 1] = 0            
        return field

    def movable(self, field):
        for i in self.shape:
            next_block = self.row + i[1] + 1
            if next_block > len(field[0]) - 1:
                return False
            elif next_block < 0:
                return "game over"
            elif field[self.column+i[0]][self.row+i[1]+1]!= 0:
                return False
            
        return True

    def stop(self, field):
        for i in self.shape:
            field[self.column + i[0]][self.row + i[1]] = 2
        return field