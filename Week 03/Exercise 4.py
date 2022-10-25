def read_nonempty_string(text):
    something_is_wrong = True
    file_name = input(text)
    while something_is_wrong:
        if len(file_name) > 0:
            something_is_wrong == False
        else:
            print("Error, please try again.")
            file_name = input(text)
    return file_name


def determine_grade(mark):
    grade = ""
    if mark >= 70:
        print("H1")
    elif 70 > mark >= 60:
        print("H2.1")
    elif 60 > mark >= 50:
        print("H2.2")
    elif 50 > mark >= 40:
        print("Pass")
    elif mark < 40:
        print("Fail")
    return grade


def main():
    input_filename = read_nonempty_string("Enter file name >>> ")

main()