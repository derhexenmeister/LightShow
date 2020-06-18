import piper_light_show
import time

def red(intensity):
    return intensity*16
def green(intensity):
    return intensity*4
def blue(intensity):
    return intensity*1
def cyan(intensity):
    return green(intensity)+blue(intensity)
def magenta(intensity):
    return red(intensity)+blue(intensity)
def yellow(intensity):
    return red(intensity)+green(intensity)
def white(intensity):
    return red(intensity)+green(intensity)+blue(intensity)

piper_light_show.init()
screen = piper_light_show.Pix()

while True:
    ################################################################################
    # First Phase
    text = piper_light_show.Pix.from_text("Hello world!", color=piper_light_show.RED, bgcolor=piper_light_show.BLUE)
    screen.box(color=piper_light_show.BLUE, x=0, y=0, width=8, height=8)

    start = time.monotonic()
    while time.monotonic() - start < 5:
        for dx in range(-8, text.width):
            screen.blit(text, -dx, 1)
            piper_light_show.show(screen)
            piper_light_show.tick(1/12)
            
    ################################################################################
    # Second Phase

    # Try orange for undrawn pixels
    #
    screen.box(color=52, x=0, y=0, width=8, height=8)

    for x in range(4):
        screen.pixel(x, 0, color=red(x))
        screen.pixel(x+4, 0, color=red(3-x))
        screen.pixel(x, 1, color=green(x))
        screen.pixel(x+4, 1, color=green(3-x))
        screen.pixel(x, 2, color=blue(x))
        screen.pixel(x+4, 2, color=blue(3-x))
        screen.pixel(x, 3, color=cyan(x))
        screen.pixel(x+4, 3, color=cyan(3-x))
        screen.pixel(x, 4, color=magenta(x))
        screen.pixel(x+4, 4, color=magenta(3-x))
        screen.pixel(x, 5, color=yellow(x))
        screen.pixel(x+4, 5, color=yellow(3-x))
        screen.pixel(x, 6, color=white(x))
        screen.pixel(x+4, 6, color=white(3-x))


    piper_light_show.show(screen)

    time.sleep(5)
        
    ################################################################################
    # Third Phase - show all colors on one screen (could sort?)
    #
    z = 0
    for x in range(8):
     for y in range(8):
        screen.pixel(x, y, color=z)
        z = z + 1

    piper_light_show.show(screen)

    time.sleep(5)

    ################################################################################
    # Fourth phase - sorted by value, hue, saturation

    background = piper_light_show.Pix.from_iter((
        (0,  21, 16, 20,  4,  5,  1, 17), 
        (42, 37, 32, 36, 41, 40, 24, 25), 
        (8,   9, 26, 10,  6, 22,  2, 18), 
        (38, 34, 33, 63, 58, 53, 48, 52), 
        (57, 56, 62, 61, 60, 44, 45, 28), 
        (46, 29, 12, 13, 30, 14, 47, 31), 
        (15, 11, 27,  7, 43, 23,  3, 19), 
        (39, 35, 59, 55, 51, 50, 54, 49), 
    ))

    piper_light_show.show(background)

    time.sleep(5)

    ################################################################################
    # Fifth Phase - TODO investigate glitch when this starts up

    ball = piper_light_show.Pix.from_iter((
        (0, 0), # black
        (0, 0),
    ))

    background = piper_light_show.Pix.from_iter((
        (piper_light_show.RED, piper_light_show.GREEN, piper_light_show.BLUE, piper_light_show.CYAN, piper_light_show.MAGENTA, piper_light_show.YELLOW, piper_light_show.RED, piper_light_show.GREEN),
        (piper_light_show.GREEN, piper_light_show.BLUE, piper_light_show.CYAN, piper_light_show.MAGENTA, piper_light_show.YELLOW, piper_light_show.RED, piper_light_show.GREEN, piper_light_show.BLUE),
        (piper_light_show.BLUE, piper_light_show.CYAN, piper_light_show.MAGENTA, piper_light_show.YELLOW, piper_light_show.RED, piper_light_show.GREEN, piper_light_show.BLUE, piper_light_show.CYAN),
        (piper_light_show.CYAN, piper_light_show.MAGENTA, piper_light_show.YELLOW, piper_light_show.RED, piper_light_show.GREEN, piper_light_show.BLUE, piper_light_show.CYAN, piper_light_show.MAGENTA),
        (piper_light_show.MAGENTA, piper_light_show.YELLOW, piper_light_show.RED, piper_light_show.GREEN, piper_light_show.BLUE, piper_light_show.CYAN, piper_light_show.MAGENTA, piper_light_show.YELLOW),
        (piper_light_show.YELLOW, piper_light_show.RED, piper_light_show.GREEN, piper_light_show.BLUE, piper_light_show.CYAN, piper_light_show.MAGENTA, piper_light_show.YELLOW, piper_light_show.RED),
        (piper_light_show.RED, piper_light_show.GREEN, piper_light_show.BLUE, piper_light_show.CYAN, piper_light_show.MAGENTA, piper_light_show.YELLOW, piper_light_show.RED, piper_light_show.GREEN),
        (piper_light_show.GREEN, piper_light_show.BLUE, piper_light_show.CYAN, piper_light_show.MAGENTA, piper_light_show.YELLOW, piper_light_show.RED, piper_light_show.GREEN, piper_light_show.BLUE),
    ))

    x = 3
    y = 1
    dx = 1
    dy = 1

    start = time.monotonic()
    while time.monotonic() - start < 5:
        screen.blit(background)
        if not 0 < x < 6:
            dx = -dx
        if not 0 < y < 6:
            dy = -dy
        x += dx
        y += dy
        screen.blit(ball, x, y)
        piper_light_show.show(screen)
        piper_light_show.tick(4/12)

    ################################################################################
    # Sixth Phase

    background = piper_light_show.Pix.from_iter((
        (0, 0, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 0, 0, 0),
    ))

    ball = piper_light_show.Pix.from_iter((
        (63, 42), # different levels of white
        (42, 21), # UGLY, but easier to see white ball
    ))

    start = time.monotonic()
    while time.monotonic() - start < 5:
        screen.blit(background)
        if not 0 < x < 6:
            dx = -dx
        if not 0 < y < 6:
            dy = -dy
        x += dx
        y += dy
        screen.blit(ball, x, y)
        piper_light_show.show(screen)
        piper_light_show.tick(4/12)

