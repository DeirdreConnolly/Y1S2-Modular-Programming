def read_nonnegative_float(prompt):
    something_is_wrong = True
    while something_is_wrong:
        try:
            number = float(input(prompt))
            if number >= 0:
                something_is_wrong = False
            else:
                print("Non-negative numbers please...")
        except:
            print("Must be numeric...")
    return number


def main():
    weight = read_nonnegative_float("Weight of flour (g) >>> ")
    print("You have specified for", weight, "grammes.")


main()