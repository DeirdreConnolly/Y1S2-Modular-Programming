def read_nonnegative_integer(prompt):
    something_is_wrong = True
    while something_is_wrong:
        try:
            number = int(input(prompt))
            if number >= 0:
                something_is_wrong = False
            else:
                print("Non-negative numbers please...")
        except:
            print("Must be numeric...")
    return number


def main():
    number_of_books = read_nonnegative_integer("Number of books >>> ")
    print("You have asked for", number_of_books, "books.")

    number_of_children = read_nonnegative_integer("How many children >>> ")
    print("You have specified ", number_of_children, "children")

main()