import pygame
from config import CELL_SIZE, WHITE

class Cell:
    """Represents a single cell in the maze grid."""

    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.visited = False

        # All 4 walls start as present
        self.walls = {
            "N": True,
            "S": True,
            "E": True,
            "W": True
        }

    def draw(self, screen):
        x = self.col * CELL_SIZE
        y = self.row * CELL_SIZE

        wall_configs = {
            "N": ((x,              y             ), (x + CELL_SIZE, y             )),
            "S": ((x,              y + CELL_SIZE ), (x + CELL_SIZE, y + CELL_SIZE )),
            "E": ((x + CELL_SIZE,  y             ), (x + CELL_SIZE, y + CELL_SIZE )),
            "W": ((x,              y             ), (x,             y + CELL_SIZE )),
        }

        for direction, (start, end) in wall_configs.items():
            if self.walls[direction]:
                pygame.draw.line(screen, WHITE, start, end, 2)