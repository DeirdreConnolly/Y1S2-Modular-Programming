def print_line(n):
    print("*" * n)


def print_square(n):
    for k in range(n):
        print_line(n)


def main():
    print_square(5)


main()
