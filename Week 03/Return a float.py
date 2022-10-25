def read_nonnegative_float(prompt):
    something_is_wrong = True
    while something_is_wrong:
        try:
            number = int(input(prompt))
            if number >= 0:
                something_is_wrong = False
            else:
                print("Error, must be a positive number")
        except:
            print("Error, must be numeric")
    return number


def calculate_rectangle(length, width):
    result = (length * width)
    return result


def rectangle():
    length = read_nonnegative_float("Length of rectangle in cm: ")
    width = read_nonnegative_float("Width of rectangle in cm: ")
    area = calculate_rectangle(length, width)
    return area

area = rectangle()
print(str(area) + "cm^2")