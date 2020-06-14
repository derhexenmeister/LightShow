import spi_595

spi_595.init()

pix = spi_595.BLACK
screen = spi_595.Pix.from_iter((
    (pix, pix, pix, pix, pix, pix, pix, pix),
    (pix, pix, pix, pix, pix, pix, pix, pix),
    (pix, pix, pix, pix, pix, pix, pix, pix),
    (pix, pix, pix, pix, pix, pix, pix, pix),
    (pix, pix, pix, pix, pix, pix, pix, pix),
    (pix, pix, pix, pix, pix, pix, pix, pix),
    (pix, pix, pix, pix, pix, pix, pix, pix),
    (pix, pix, pix, pix, pix, pix, pix, pix),
))

#screen.box(color=spi_595.RED, x=0, y=0, width=4, height=4)
#screen.box(color=spi_595.GREEN, x=4, y=0, width=4, height=4)
#screen.box(color=spi_595.BLUE, x=0, y=4, width=4, height=4)
#screen.box(color=spi_595.CYAN, x=4, y=4, width=4, height=4)

#screen.box(color=spi_595.MAGENTA, x=2, y=2, width=2, height=2)
#screen.box(color=spi_595.YELLOW, x=2, y=4, width=2, height=2)
#screen.box(color=spi_595.WHITE, x=4, y=4, width=2, height=2)
#screen.box(color=spi_595.BLACK, x=4, y=2, width=2, height=2)

#screen.pixel(0, 0, color=spi_595.WHITE)
#screen.pixel(0, 7, color=spi_595.YELLOW)

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
#screen.box(color=52, x=0, y=0, width=8, height=1)
screen.box(color=52, x=0, y=7, width=8, height=1)

while True:
    spi_595.show(screen)
    spi_595.tick(1/6)

