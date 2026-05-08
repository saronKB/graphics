import pygame
import sys
from config import WIDTH, HEIGHT, FPS, CELL_SIZE, YELLOW, MAGENTA, BLUE, GREEN
from maze import maze, draw_maze, reset_visited
from generator import generate_maze
from solver import solve_maze

# =========================
# SETUP
# =========================

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Runner")
clock = pygame.time.Clock()

# =========================
# RUN MAZE
# =========================

# Step 1 — Generate
generate_maze(screen)

# Step 2 — Reset visited so solver starts fresh
reset_visited()

# Step 3 — Define start and end
start = (0, 0)
end   = (len(maze) - 1, len(maze[0]) - 1)

# Step 4 — Solve
path, dead_ends = solve_maze(screen, start, end)

# =========================
# FINAL DISPLAY LOOP
# =========================

def draw_final(path, dead_ends, start, end):
    """Draw the completed maze with solution and markers."""
    draw_maze(screen)

    # Dead ends
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

    # Solution path
    if path:
        for pr, pc in path:
            pygame.draw.rect(
                screen, GREEN,
                (
                    pc * CELL_SIZE + CELL_SIZE // 4,
                    pr * CELL_SIZE + CELL_SIZE // 4,
                    CELL_SIZE // 2,
                    CELL_SIZE // 2
                )
            )

    # Start marker — yellow
    sr, sc = start
    pygame.draw.circle(
        screen, YELLOW,
        (sc * CELL_SIZE + CELL_SIZE // 2, sr * CELL_SIZE + CELL_SIZE // 2),
        CELL_SIZE // 4
    )

    # End marker — magenta
    er, ec = end
    pygame.draw.circle(
        screen, MAGENTA,
        (ec * CELL_SIZE + CELL_SIZE // 2, er * CELL_SIZE + CELL_SIZE // 2),
        CELL_SIZE // 4
    )

    pygame.display.update()


running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw_final(path, dead_ends, start, end)

pygame.quit()