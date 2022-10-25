def sing(name):
    sing_line()
    sing_line()
    print("Happy Birthday dear", name)
    sing_line()


def sing_line():
    print("Happy Birthday to you!")


def main():
    childs_name = input("What is the child's name?")
    sing(childs_name)


main()

