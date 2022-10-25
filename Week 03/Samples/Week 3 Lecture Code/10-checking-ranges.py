def check_if_percentage(x):
    return 0 <= x <= 100


def read_percentage_float(prompt):
    something_is_wrong = True
    while something_is_wrong:
        try:
            number = float(input(prompt))
            if check_if_percentage(number):
                something_is_wrong = False
            else:
                print("Values 0-100 please...")
        except:
            print("Must be numeric...")
    return number


def print_grade(mark):
    if mark < 40:
        print("Fail")
    else:
        print("Pass")


def main():
    exam_mark = read_percentage_float("Exam grade >>> ")
    print_grade(exam_mark)


main()