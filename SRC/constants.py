WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GREY = (100, 100, 100)
LIGHT_GREY = (150, 150, 150)
BACKGROUND_COLOR = GREY

ORIGIN = (0,0)

BLOCK_SIZE = 40

PADDING = BLOCK_SIZE

SCREEN_WIDTH = 19 * BLOCK_SIZE
SCREEN_HEIGHT = 12 * BLOCK_SIZE
SCREEN_DIMENSIONS = (SCREEN_WIDTH, SCREEN_HEIGHT)

PLAYGROUND_WIDTH = 11 * BLOCK_SIZE
PLAYGROUND_HEIGHT = PLAYGROUND_WIDTH
PLAYGROUND_DIMENSIONS = (PLAYGROUND_WIDTH, PLAYGROUND_HEIGHT)
PLAYGROUND_X = PADDING
PLAYGROUND_Y = 0
PLAYGROUND_POSITION = (PLAYGROUND_X, PLAYGROUND_Y)
PLAYGROUND_RECT = (PLAYGROUND_X, PLAYGROUND_Y, PLAYGROUND_WIDTH, PLAYGROUND_HEIGHT)


MENU_WIDTH = 5 * BLOCK_SIZE
MENU_HEIGHT = PLAYGROUND_HEIGHT - 2 * PADDING
MENU_X = PLAYGROUND_X + PLAYGROUND_WIDTH + PADDING
MENU_Y = PADDING
MENU_DIMENSIONS = (MENU_WIDTH, MENU_HEIGHT)
MENU_POSITION = (MENU_X, MENU_Y)
MENU_RECT = (MENU_X, MENU_Y, MENU_WIDTH, MENU_HEIGHT)
