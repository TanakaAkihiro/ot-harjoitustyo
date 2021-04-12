class Block:
    def __init__(self):
        self.shape = [[-1, 0], [0,0], [1,0], [2,0]]
        self.row = 1
        self.column = 5
    
    def move(self, field):
        if self.movable(field):
            print(self.row)
            self.row += 1
            for i in self.shape:
                field[self.column + i[0]][self.row + i[1] - 1] = 0
    
    def movable(self, field):
        for i in self.shape:
            if self.row + i[1] + 1 > len(field[0]):
                field[self.column + i[0]][self.row + i[1]] = 2
                return False
            elif self.row + i[1] + 1 < 0:
                return False
            elif field[self.column+i[0]][self.row+i[1]+1]!= 0:
                field[self.column+i[0]][self.row+i[1]+1] = 2
                return False
            
        return True
