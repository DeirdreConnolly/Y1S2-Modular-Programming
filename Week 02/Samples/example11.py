def main():
    value = 99
    print("The value is", value)
    change_me(value)
    print("Back to main... value is", value)


def change_me(arg):
    print("I will attempt to change the value")
    arg = 0
    print("The value is now", arg )


main()