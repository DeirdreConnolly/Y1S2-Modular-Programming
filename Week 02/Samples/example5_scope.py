def solid_line():
    number_of_spaces = 10
    edge_character = '+'    # different variable to that in gappy_line()
    print(edge_character, number_of_spaces * "-", edge_character, sep="")


def gappy_line():
    number_of_dashes = 10
    edge_character = "-"    # different variable to that in solid_line()
    print(edge_character,number_of_dashes*" ", edge_character, sep="")


def main():
    solid_line()
    for k in range(3):
        gappy_line()
    solid_line()


main()