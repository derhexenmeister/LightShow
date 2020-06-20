# From https://github.com/pewpew-game/game-boulder/blob/master/boulder.py
#
import piper_light_show as ls

VOID = 0
WALL = 1
SOIL = 2
ROCK = 3
HERO = 4
GEM1 = 5
GEM2 = 6


ls.init(dpad=True)
screen = ls.Pix.from_iter((
    (1, 1, 1, 4, 1, 1, 1, 1),
    (1, 2, 2, 2, 3, 0, 2, 1),
    (1, 1, 3, 1, 2, 5, 2, 1),
    (1, 2, 2, 1, 2, 1, 1, 1),
    (1, 2, 0, 3, 2, 3, 2, 1),
    (1, 2, 0, 5, 2, 2, 2, 1),
    (1, 2, 2, 2, 2, 2, 2, 1),
    (1, 1, 1, 1, 1, 1, 1, 1),
))

blink = 1
dead = False
for y in range(8):
    for x in range(8):
        if screen.pixel(x, y) == 4:
            break;
    else:
        continue
    break

while not dead:
    screen.pixel(x, y, VOID)
    pressed = ls.keys()
    dx = 0
    dy = 0
    if pressed & ls.K_UP:
        dy = -1
    elif pressed & ls.K_DOWN:
        dy = 1
    elif pressed & ls.K_LEFT:
        dx = -1
    elif pressed & ls.K_RIGHT:
        dx = 1
    if screen.pixel(x + dx, y + dy) not in {WALL, ROCK}:
        x += dx
        y += dy
    elif screen.pixel(x + dx, y + dy) == ROCK and dy == 0:
        if screen.pixel(x + dx + dx, y + dy + dy) == VOID:
            screen.pixel(x + dx + dx, y + dy + dy, ROCK)
            screen.pixel(x + dx, y + dy, VOID)
            x += dx
            y += dy
    count = 0
    for a in range(8):
        for b in range(7, -1, -1):
            if (screen.pixel(a, b) == ROCK and
                    screen.pixel(a, b + 1) == VOID and
                    (a, b + 1) != (x, y)):
                screen.pixel(a, b, VOID)
                screen.pixel(a, b + 1, ROCK)
                if (a, b + 2) == (x, y):
                    dead = True
            if screen.pixel(a, b) in {GEM1, GEM2}:
                screen.pixel(a, b, GEM1 if blink else GEM2)
                count += 1
    if count == 0:
        break
    screen.pixel(x, y, 3 if blink else HERO)
    blink = not blink
    ls.show(screen)
    ls.tick(1 / 6)

