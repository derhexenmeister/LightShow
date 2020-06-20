# From https://github.com/pewpew-game/pewpew/blob/master/games/tetris.py

import random
import piper_light_show as ls

BLACK   = ls.BLACK
RED     = ls.RED
GREEN   = ls.GREEN
BLUE    = ls.BLUE
CYAN    = ls.CYAN
MAGENTA = ls.MAGENTA
YELLOW  = ls.YELLOW
ORANGE  = 52

BRICKS = [
    ls.Pix.from_iter([[RED, RED], [RED, RED]]),
    ls.Pix.from_iter([[BLACK, GREEN], [GREEN, GREEN], [BLACK, GREEN]]),
    ls.Pix.from_iter([[BLACK, BLUE], [BLUE, BLUE], [BLUE, BLACK]]),
    ls.Pix.from_iter([[CYAN, BLACK], [CYAN, CYAN], [BLACK, CYAN]]),
    ls.Pix.from_iter([[MAGENTA, MAGENTA], [BLACK, MAGENTA], [BLACK, MAGENTA]]),
    ls.Pix.from_iter([[YELLOW, YELLOW], [YELLOW, BLACK], [YELLOW, BLACK]]),
    ls.Pix.from_iter([[ORANGE], [ORANGE], [ORANGE], [ORANGE]]),
    ls.Pix.from_iter([[ORANGE], [ORANGE], [ORANGE], [ORANGE]]),
]

def is_colliding(board, brick, brick_x, brick_y):
    for y in range(brick.height):
        for x in range(brick.width):
            if (brick.pixel(x, y) and
                    board.pixel(brick_x + x + 1, brick_y + y + 3)):
                return True
    return False

def debounce():
    for i in range(100):
        ls.tick(1/100)
        if not ls.keys():
            return

ls.init(dpad=True)

while True:
    screen = ls.Pix(width=8, height=8)
    #screen.box(color=YELLOW, x=6, y=0, width=2, height=8) # What was this???
    next_brick = BRICKS[random.getrandbits(3)]
    board = ls.Pix(width=8, height=12)
    board.box(color=CYAN)
    board.box(color=BLACK, x=1, y=0, width=6, height=11)

    while True:
        brick = next_brick
        next_brick = BRICKS[random.getrandbits(3)]  # 0-7
        screen.box(color=BLACK, x=6, y=0, width=2, height=5)
        screen.blit(next_brick, dx=6, dy=0)
        brick_x = 2
        brick_y = -3
        while True:
            if is_colliding(board, brick, brick_x, brick_y):
                break
            for turn in range(4):
                keys = ls.keys()
                if (keys & ls.K_LEFT and
                        not is_colliding(board, brick, brick_x - 1, brick_y)):
                    brick_x -= 1
                    debounce()
                elif (keys & ls.K_RIGHT and
                        not is_colliding(board, brick, brick_x + 1, brick_y)):
                    brick_x += 1
                    debounce()
                #if keys & ls.K_O:
                if keys & ls.K_UP:
                    new_brick = ls.Pix.from_iter([
                            [brick.pixel(brick.width - y - 1, x)
                                for x in range(brick.height)]
                            for y in range(brick.width)
                        ])
                    if not is_colliding(board, new_brick, brick_x, brick_y):
                        brick = new_brick
                    debounce()
                elif keys & ls.K_X:
                    new_brick = ls.Pix.from_iter([
                            [brick.pixel(y, brick.height - x -1)
                                for x in range(brick.height)]
                            for y in range(brick.width)
                        ])
                    if not is_colliding(board, new_brick, brick_x, brick_y):
                        brick = new_brick
                    debounce()
                screen.blit(board, dx=0, dy=0, x=1, y=3, width=6, height=8)
                screen.blit(brick, dx=brick_x, dy=brick_y, key=0)
                ls.show(screen)
                if keys & ls.K_DOWN:
                    break
                ls.tick(1/4)
            brick_y += 1
        board.blit(brick, dx=brick_x + 1, dy=brick_y - 1 + 3, key=0)
        debounce()
        if brick_y < 0:
            break
        for row in range(11):
            if sum(1 for x in range(1, 7) if board.pixel(x, row)) != 6:
                continue
            for y in range(row, 0, -1):
                for x in range(1, 7):
                    board.pixel(x, y, board.pixel(x, y - 1))

    screen.box(0, 6, 0, 2, 5)
    for y in range(7, -1, -1):
        screen.box(3, x=0, y=y, width=6, height=1)
        ls.show(screen)
        ls.tick(1/4)
