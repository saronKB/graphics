# Game configuration and color constants

ROWS = 20
COLS = 20
CELL_SIZE = 30

WIDTH = COLS * CELL_SIZE
HEIGHT = ROWS * CELL_SIZE

FPS = 60

# ✅ Humanized — smooth and natural to watch
GENERATION_DELAY = 18
SOLVE_DELAY_NORMAL = 22
SOLVE_DELAY_DEAD_END = 50

# Colors
BLACK      = (0,   0,   0  )
WHITE      = (255, 255, 255)
RED        = (255, 50,  50 )   # player dot
BLUE       = (50,  100, 255)   # dead ends
GREEN      = (0,   220, 100)   # solution path
GRAY       = (40,  40,  40 )
YELLOW     = (255, 255, 0  )   # start
MAGENTA    = (255, 0,   255)   # end
TRAIL      = (30,  30,  80 )   # faint trail color