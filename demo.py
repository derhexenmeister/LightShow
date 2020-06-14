import spi_595
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

spi_595.init()
screen = spi_595.Pix()

################################################################################
# First Phase
background = spi_595.Pix.from_iter((
    (0,0,0,0,0,0,0,0),
    (0,0,0,0,0,0,0,0),
    (0,0,0,0,0,0,0,0),
    (0,0,0,0,0,0,0,0),
    (0,0,0,0,0,0,0,0),
    (0,0,0,0,0,0,0,0),
    (0,0,0,0,0,0,0,0),
    (0,0,0,0,0,0,0,0),
))

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

# Try orange for bottom row. It seems to show some
# fading. May be due to current sharing for column?
#
screen.box(color=52, x=0, y=7, width=8, height=1)

spi_595.show(screen)

time.sleep(10)
    
################################################################################
# Second Phase - show all colors on one screen (could sort?)
#
z = 0
for x in range(8):
 for y in range(8):
    screen.pixel(x, y, color=z)
    z = z + 1

spi_595.show(screen)

time.sleep(10)

################################################################################
# Third Phase

ball = spi_595.Pix.from_iter((
    (0,  0,  0, 0), # black outline and
    (0, 63, 42, 0), # different levels of white
    (0, 42, 21, 0), # UGLY, but easier to see white ball
    (0,  0,  0, 0),
))

background = spi_595.Pix.from_iter((
    (spi_595.RED, spi_595.GREEN, spi_595.BLUE, spi_595.CYAN, spi_595.MAGENTA, spi_595.YELLOW, spi_595.RED, spi_595.GREEN),
    (spi_595.GREEN, spi_595.BLUE, spi_595.CYAN, spi_595.MAGENTA, spi_595.YELLOW, spi_595.RED, spi_595.GREEN, spi_595.BLUE),
    (spi_595.BLUE, spi_595.CYAN, spi_595.MAGENTA, spi_595.YELLOW, spi_595.RED, spi_595.GREEN, spi_595.BLUE, spi_595.CYAN),
    (spi_595.CYAN, spi_595.MAGENTA, spi_595.YELLOW, spi_595.RED, spi_595.GREEN, spi_595.BLUE, spi_595.CYAN, spi_595.MAGENTA),
    (spi_595.MAGENTA, spi_595.YELLOW, spi_595.RED, spi_595.GREEN, spi_595.BLUE, spi_595.CYAN, spi_595.MAGENTA, spi_595.YELLOW),
    (spi_595.YELLOW, spi_595.RED, spi_595.GREEN, spi_595.BLUE, spi_595.CYAN, spi_595.MAGENTA, spi_595.YELLOW, spi_595.RED),
    (spi_595.RED, spi_595.GREEN, spi_595.BLUE, spi_595.CYAN, spi_595.MAGENTA, spi_595.YELLOW, spi_595.RED, spi_595.GREEN),
    (spi_595.GREEN, spi_595.BLUE, spi_595.CYAN, spi_595.MAGENTA, spi_595.YELLOW, spi_595.RED, spi_595.GREEN, spi_595.BLUE),
))

x = 3
y = 1
dx = 1
dy = 1
while True:
    screen.blit(background)
    if not -1 < x < 5:
        dx = -dx
    if not -1 < y < 5:
        dy = -dy
    x += dx
    y += dy
    screen.blit(ball, x, y)
    spi_595.show(screen)
    spi_595.tick(4/12)
 
