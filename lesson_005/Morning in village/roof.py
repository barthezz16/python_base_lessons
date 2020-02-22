import simple_draw as sd
sd.resolution = (1200, 800)

def roof_draw():
    left_bottom_x = 300
    left_bottom_y = 200
    left_bottom = sd.get_point(left_bottom_x, left_bottom_y)
    top_x = 525
    top_y = 300
    top = sd.get_point(top_x, top_y)
    right_bottom_x = 750
    right_bottom_y = 200
    right_bottom = sd.get_point(right_bottom_x, right_bottom_y)
    point_list = [left_bottom, right_bottom, top]
    sd.polygon(point_list=point_list, color=sd.COLOR_ORANGE, width=0)


if __name__ == '__main__':
    roof_draw()

