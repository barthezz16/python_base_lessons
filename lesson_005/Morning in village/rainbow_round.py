import simple_draw as sd
sd.resolution = (1200, 800)
rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)


def rainbow_round_draw():
    x = 200
    y = -200
    radius = 1100
    for color in rainbow_colors:
        radius += 15
        start_point = sd.get_point(x, y)
        sd.circle(center_position=start_point, radius=radius, color=color, width=15)

