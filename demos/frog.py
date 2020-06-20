# From https://github.com/pewpew-game/piper_light_showpiper_light_show/blob/master/games/frog.py
#
import piper_light_show as ls

ls.init(dpad=True)

while True:
    screen = ls.Pix()
    x, y = 4, 7
    grass = ls.Pix.from_iter(([ls.GREEN]*8,))
    pedestrians = ls.Pix.from_iter(([0, ls.YELLOW, 0, 0] * 4,))
    cars = ls.Pix.from_iter(([0, ls.RED, ls.RED, 0] * 4,))
    screen.blit(grass, 0, 0)
    screen.blit(grass, 0, 3)
    screen.blit(grass, 0, 4)
    screen.blit(grass, 0, 7)
    old_pixel = screen.pixel(x, y)
    traffic = 0
    alive = True
    pressing = False
    while alive:
        keys = ls.keys()
        screen.pixel(x, y, old_pixel)

        if not pressing:
            if keys & ls.K_UP and y > 0:
                y -= 1
            elif keys & ls.K_DOWN and y < 7:
                y += 1
            if keys & ls.K_LEFT and x > 0:
                x -= 1
            elif keys & ls.K_RIGHT and x < 7:
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
        if old_pixel == ls.RED or old_pixel == ls.YELLOW:
            alive = False
        traffic = (traffic + 1) % 32
        screen.pixel(x, y, ls.BLUE)
        ls.show(screen)
        ls.tick(1/6)

    text = ls.Pix.from_text("Game over!", color=ls.RED, bgcolor=ls.WHITE)
    for dx in range(-8, text.width):
        screen.blit(text, -dx, 1)
        ls.show(screen)
        ls.tick(1/12)
