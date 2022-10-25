def solid_line():
    print("+", 10 * "-", "+", sep="")


def gappy_line():
    print("-",10*" ", "-", sep="")


def main():
    solid_line()
    for k in range(3):
        gappy_line()
    solid_line()

main()