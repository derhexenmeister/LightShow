# From https://github.com/pewpew-game/pewpew/blob/master/games/tetris.py

import random
import piper_light_show


BLACK   = piper_light_show.BLACK
RED     = piper_light_show.RED
GREEN   = piper_light_show.GREEN
BLUE    = piper_light_show.BLUE
CYAN    = piper_light_show.CYAN
MAGENTA = piper_light_show.MAGENTA
YELLOW  = piper_light_show.YELLOW

BRICKS = [
    piper_light_show.Pix.from_iter([[RED, RED], [RED, RED]]),
    piper_light_show.Pix.from_iter([[BLACK, GREEN], [GREEN, GREEN], [BLACK, GREEN]]),
    piper_light_show.Pix.from_iter([[BLACK, YELLOW], [YELLOW, YELLOW], [YELLOW, BLACK]]),
    piper_light_show.Pix.from_iter([[GREEN, BLACK], [GREEN, GREEN], [BLACK, GREEN]]),
    piper_light_show.Pix.from_iter([[GREEN, GREEN], [BLACK, GREEN], [BLACK, GREEN]]),
    piper_light_show.Pix.from_iter([[YELLOW, YELLOW], [YELLOW, BLACK], [YELLOW, BLACK]]),
    piper_light_show.Pix.from_iter([[RED], [RED], [RED], [RED]]),
    piper_light_show.Pix.from_iter([[RED], [RED], [RED], [RED]]),
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
        piper_light_show.tick(1/100)
        if not piper_light_show.keys():
            return

piper_light_show.init()

while True:
    screen = piper_light_show.Pix(width=8, height=8)
    screen.box(color=YELLOW, x=6, y=0, width=2, height=8)
    next_brick = BRICKS[random.getrandbits(3)]
    board = piper_light_show.Pix(width=8, height=12)
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
                keys = piper_light_show.keys()
                if (keys & piper_light_show.K_LEFT and
                        not is_colliding(board, brick, brick_x - 1, brick_y)):
                    brick_x -= 1
                    debounce()
                elif (keys & piper_light_show.K_RIGHT and
                        not is_colliding(board, brick, brick_x + 1, brick_y)):
                    brick_x += 1
                    debounce()
                #if keys & piper_light_show.K_O:
                if keys & piper_light_show.K_UP:
                    new_brick = piper_light_show.Pix.from_iter([
                            [brick.pixel(brick.width - y - 1, x)
                                for x in range(brick.height)]
                            for y in range(brick.width)
                        ])
                    if not is_colliding(board, new_brick, brick_x, brick_y):
                        brick = new_brick
                    debounce()
                elif keys & piper_light_show.K_X:
                    new_brick = piper_light_show.Pix.from_iter([
                            [brick.pixel(y, brick.height - x -1)
                                for x in range(brick.height)]
                            for y in range(brick.width)
                        ])
                    if not is_colliding(board, new_brick, brick_x, brick_y):
                        brick = new_brick
                    debounce()
                screen.blit(board, dx=0, dy=0, x=1, y=3, width=6, height=8)
                screen.blit(brick, dx=brick_x, dy=brick_y, key=0)
                piper_light_show.show(screen)
                if keys & piper_light_show.K_DOWN:
                    break
                piper_light_show.tick(1/4)
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
        piper_light_show.show(screen)
        piper_light_show.tick(1/4)
