import pygame
import random
import sys
from config import (
    ROWS, COLS, CELL_SIZE,
    RED, BLUE, GREEN,
    SOLVE_DELAY_NORMAL,
    SOLVE_DELAY_DEAD_END
)
from maze import maze, draw_maze, get_possible_moves

def solve_maze(screen, start, end):
    stack = [start]
    dead_ends = []
    step = 0

    while stack:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        current = stack[-1]
        row, col = current
        maze[row][col].visited = True

        if current == end:
            return stack, dead_ends

        moves = get_possible_moves(row, col)
        random.shuffle(moves)

        moved = False
        for nr, nc in moves:
            if not maze[nr][nc].visited:
                stack.append((nr, nc))
                moved = True
                break

        hit_dead_end = not moved
        if hit_dead_end:
            dead_ends.append(current)
            stack.pop()

        step += 1

        # ✅ only draw every 4 steps — much faster traversal
        if step % 2 == 0 or hit_dead_end:
            draw_maze(screen)

            for dr, dc in dead_ends:
                pygame.draw.rect(
                    screen, BLUE,
                    (
                        dc * CELL_SIZE + CELL_SIZE // 4,
                        dr * CELL_SIZE + CELL_SIZE // 4,
                        CELL_SIZE // 2,
                        CELL_SIZE // 2
                    )
                )

            for pr, pc in stack:
                pygame.draw.rect(
                    screen, GREEN,
                    (
                        pc * CELL_SIZE + CELL_SIZE // 4,
                        pr * CELL_SIZE + CELL_SIZE // 4,
                        CELL_SIZE // 2,
                        CELL_SIZE // 2
                    )
                )

            pygame.draw.circle(
                screen, RED,
                (
                    col * CELL_SIZE + CELL_SIZE // 2,
                    row * CELL_SIZE + CELL_SIZE // 2
                ),
                CELL_SIZE // 4
            )

            pygame.display.update()

            # slow at dead ends, fast otherwise
            delay = SOLVE_DELAY_DEAD_END if hit_dead_end else SOLVE_DELAY_NORMAL
            pygame.time.delay(delay)

    return None, dead_ends