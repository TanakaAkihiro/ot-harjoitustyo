import pygame
from ui.block import Block

class Gameloop:
    def __init__(self, screen, height, width):
        self.screen = screen
        self.height = height
        self.width = width
        self.new_block = True
        self.clock = pygame.time.Clock()

        self.field = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
    
    def start(self):
        self.show_screen(self.screen)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

            if self.new_block:
                block = Block()
                self.new_block = False
            
            if not block.movable(self.field):
                self.new_block = True
                self.field = block.stop(self.field)
            elif block.movable(self.field) == "gameover":
                break
            else:
                self.field = block.move(self.field)
            
            self.draw_field(self.field, self.screen)

            self.clock.tick(10)
            

    def show_screen(self, screen):
        screen.fill((255,255,255))

        for i in range(self.height):
            for j in range(self.width):
                pygame.draw.rect(screen, (0,0,0), (220 + 20*j, 100 + 20*i, 20, 20),1)

        pygame.display.flip()
    
    def draw_field(self, field, screen):
        for r in range(self.height):
            for c in range(self.width):
                pygame.draw.rect(screen, (192,192,192), (221 + 20*c, 101 + 20*r, 19, 19))
                if field[c][r] == 1:
                    pygame.draw.rect(screen, (0,0,128), (221 + 20*c, 101 + 20*r, 19, 19))
                if field[c][r] == 2:
                    pygame.draw.rect(screen, (200,0,0), (221 + 20*c, 101 + 20*r, 19, 19))
        pygame.display.flip()