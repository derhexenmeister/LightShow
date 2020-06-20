# From https://github.com/pewpew-game/pewpew/blob/master/games/snake.py
import piper_light_show as ls
import random

ls.init(dpad=True)

while True:
    screen = ls.Pix()

    game_speed = 4
    snake = [(ls.GREEN, ls.BLUE)]
    dx, dy = 1, 0
    apple_x, apple_y = 6, 4
    screen.pixel(apple_x, apple_y, ls.RED)

    while True:
        if len(snake) > 1:
            x, y = snake[-2]
            screen.pixel(x, y, 1)
        x, y = snake[-1]
        screen.pixel(x, y, 3)

        ls.show(screen)
        ls.tick(1 / game_speed)

        keys = ls.keys()
        if keys & ls.K_UP and dy == 0:
            dx, dy = 0, -1
        elif keys & ls.K_LEFT and dx == 0:
            dx, dy = -1, 0
        elif keys & ls.K_RIGHT and dx == 0:
            dx, dy = 1, 0
        elif keys & ls.K_DOWN and dy == 0:
            dx, dy = 0, 1
        x = (x + dx) % 8
        y = (y + dy) % 8

        if (x, y) in snake:
            break
        snake.append((x, y))

        if x == apple_x and y == apple_y:
            screen.pixel(apple_x, apple_y, 0)
            apple_x, apple_y = snake[0]
            while (apple_x, apple_y) in snake:
                apple_x = random.getrandbits(3)
                apple_y = random.getrandbits(3)
            screen.pixel(apple_x, apple_y, ls.RED)
            game_speed += 0.2
        else:
            x, y = snake.pop(0)
            screen.pixel(x, y, 0)

    text = ls.Pix.from_text("Game over!", color=ls.RED, bgcolor=ls.WHITE)
    for dx in range(-8, text.width):
        screen.blit(text, -dx, 1)
        ls.show(screen)
        ls.tick(1 / 12)
