def read_nonempty_string(prompt):
    something_is_wrong = True
    while something_is_wrong:
        s = input(prompt)
        if len(s) > 0:
            something_is_wrong = False
        else:
            print("Please type something...")
    return s


def main():
    firstname = read_nonempty_string("First name >>> ")
    surname = read_nonempty_string("Surname >>> ")
    print(firstname, surname)


main()