# From https://github.com/pewpew-game/piper_light_showpiper_light_show/blob/master/games/frog.py
#
import piper_light_show

piper_light_show.init()

while True:
    screen = piper_light_show.Pix()
    x, y = 4, 7
    grass = piper_light_show.Pix.from_iter(([piper_light_show.GREEN]*8,))
    pedestrians = piper_light_show.Pix.from_iter(([0, piper_light_show.YELLOW, 0, 0] * 4,))
    cars = piper_light_show.Pix.from_iter(([0, piper_light_show.RED, piper_light_show.RED, 0] * 4,))
    screen.blit(grass, 0, 0)
    screen.blit(grass, 0, 3)
    screen.blit(grass, 0, 4)
    screen.blit(grass, 0, 7)
    old_pixel = screen.pixel(x, y)
    traffic = 0
    alive = True
    pressing = False
    while alive:
        keys = piper_light_show.keys()
        screen.pixel(x, y, old_pixel)

        if not pressing:
            if keys & piper_light_show.K_UP and y > 0:
                y -= 1
            elif keys & piper_light_show.K_DOWN and y < 7:
                y += 1
            if keys & piper_light_show.K_LEFT and x > 0:
                x -= 1
            elif keys & piper_light_show.K_RIGHT and x < 7:
                x += 1
            if keys:
                pressing = True
        else:
            if not keys:
                pressing = False

        screen.blit(pedestrians, (traffic // 2) % 8 - 8, 1)
        screen.blit(cars, -((traffic // 2) % 8), 2)
        screen.blit(cars, traffic // 4 - 8, 5)
        screen.blit(pedestrians, -traffic // 4, 6)
        old_pixel = screen.pixel(x, y)
        if old_pixel == piper_light_show.RED or old_pixel == piper_light_show.YELLOW:
            alive = False
        traffic = (traffic + 1) % 32
        screen.pixel(x, y, piper_light_show.BLUE)
        piper_light_show.show(screen)
        piper_light_show.tick(1/6)

    text = piper_light_show.Pix.from_text("Game over!", color=piper_light_show.RED, bgcolor=piper_light_show.WHITE)
    for dx in range(-8, text.width):
        screen.blit(text, -dx, 1)
        piper_light_show.show(screen)
        piper_light_show.tick(1/12)
