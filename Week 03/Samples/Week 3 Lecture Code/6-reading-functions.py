def read_number_of_books():
    something_is_wrong = True
    while something_is_wrong:
        try:
            number = int(input("Number of books >>> "))
            if number >= 0:
                something_is_wrong = False
            else:
                print("Non-negative numbers please...")
        except:
            print("Must be numeric...")
    return number


def main():
    number_of_books = read_number_of_books()
    print("You have asked for", number_of_books, "books.")


main()