#  Maze Runner

A visual maze generator and solver built with Python and Pygame.
Watch the maze get carved in real time, then solved step by step.

---

## Preview
> Red dot explores →  Green marks solution → Blue marks dead ends

---



##  Structure
maze-runner/
├── config.py     # settings and colors
├── cell.py       # cell and wall logic
├── maze.py       # grid and helpers
├── generator.py  # maze generation (DFS)
├── solver.py     # maze solver (backtracking)
└── main.py       # entry point
---

## Configuration
All speed and size settings are in `config.py`:
```python
ROWS = 20
COLS = 20
GENERATION_DELAY = 18    
SOLVE_DELAY_NORMAL = 22  
```

---

##  Color Guide

| Color | Meaning |
|-------|---------|
|  Red | Current position |
|  Green | Solution path |
| Blue | Dead ends |
|  Yellow | Start |
|  Magenta | End |

---

## Requirements
- Python 3.x
- Pygame

---

