NUMBER_OF_LINES = 5
NUMBER_OF_STARS = 15


def draw_line():
    for stars in range(NUMBER_OF_STARS):
        print('*', end="")
    print()


def draw_rectangle():
    for lines in range(NUMBER_OF_LINES):
        draw_line()

def main():
    draw_rectangle()


main()