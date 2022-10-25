# This variable's scope is the whole of the file, including all functions.
WIDTH_OF_BOX = 17


def solid_line():
    edge_character = '+'    # different variable to that in gappy_line()
    print(edge_character, WIDTH_OF_BOX * "-", edge_character, sep="")


def gappy_line():
    edge_character = "-"    # different variable to that in solid_line()
    print(edge_character, WIDTH_OF_BOX * " ", edge_character, sep="")


def main():
    solid_line()
    for k in range(3):
        gappy_line()
    solid_line()


main()