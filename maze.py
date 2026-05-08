import pygame
from config import ROWS, COLS, BLACK
from cell import Cell

# Build the grid
maze = [
    [Cell(r, c) for c in range(COLS)]
    for r in range(ROWS)
]

def draw_maze(screen):
    """Clear screen and draw all cells."""
    screen.fill(BLACK)
    for r in range(ROWS):
        for c in range(COLS):
            maze[r][c].draw(screen)

def reset_visited():
    """Reset all visited flags — used before solving."""
    for r in range(ROWS):
        for c in range(COLS):
            maze[r][c].visited = False

def get_unvisited_neighbors(row, col):
    """Return list of unvisited neighbors with direction."""
    candidates = [
        ("N", row - 1, col    ),
        ("S", row + 1, col    ),
        ("E", row,     col + 1),
        ("W", row,     col - 1),
    ]
    return [
        (d, r, c)
        for d, r, c in candidates
        if 0 <= r < ROWS and 0 <= c < COLS
        and not maze[r][c].visited
    ]

def get_possible_moves(row, col):
    """Return neighbors reachable through open walls."""
    cell = maze[row][col]
    direction_map = {
        "N": (row - 1, col    ),
        "S": (row + 1, col    ),
        "E": (row,     col + 1),
        "W": (row,     col - 1),
    }
    return [
        pos for d, pos in direction_map.items()
        if not cell.walls[d]
    ]

def remove_walls(current, next_cell, direction):
    """Knock down walls between two adjacent cells."""
    opposite = {"N": "S", "S": "N", "E": "W", "W": "E"}
    current.walls[direction] = False
    next_cell.walls[opposite[direction]] = False