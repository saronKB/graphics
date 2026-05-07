import pygame
import random
import sys
from config import (
    ROWS, COLS, CELL_SIZE,
    RED, GENERATION_DELAY
)
from maze import maze, draw_maze, get_unvisited_neighbors, remove_walls

def generate_maze(screen):
    stack = []
    row, col = 0, 0
    maze[row][col].visited = True
    step = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        cell = maze[row][col]
        neighbors = get_unvisited_neighbors(row, col)

        if neighbors:
            direction, next_row, next_col = random.choice(neighbors)
            next_cell = maze[next_row][next_col]
            stack.append((row, col))
            remove_walls(cell, next_cell, direction)
            row, col = next_row, next_col
            maze[row][col].visited = True

        elif stack:
            row, col = stack.pop()

        else:
            break

        step += 1

        # ✅ only draw every 4 steps — much faster traversal
        if step % 2 == 0:
            draw_maze(screen)
            cx = col * CELL_SIZE + CELL_SIZE // 2
            cy = row * CELL_SIZE + CELL_SIZE // 2
            pygame.draw.circle(screen, RED, (cx, cy), CELL_SIZE // 4)
            pygame.display.update()
            pygame.time.delay(GENERATION_DELAY)

    # ✅ always draw final state when done
    draw_maze(screen)
    pygame.display.update()