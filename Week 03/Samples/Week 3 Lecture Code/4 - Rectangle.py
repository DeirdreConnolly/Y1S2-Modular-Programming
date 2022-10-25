def print_line(n):
    print("*" * n)


def print_square(n):
    for k in range(n):
        print_line(n)


def print_rectangle(w, h):
    for k in range(h):
        print_line(w)


def main():
    print_square(5)
    print()
    print_rectangle(3,5)
    print()
    print_rectangle(5, 3)


main()
