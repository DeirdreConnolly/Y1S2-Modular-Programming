# File Name:    SampleExam_Q1.py
# Author:       Deirdre Connolly
# Description:  Q1


def get_dob():
    day = input("Enter date >>> ")
    month = input("Enter month >>> ")
    year = input("Enter year >>> ")

    print("Day >>> " + day)
    print("Month >>> " + month)
    print("Year >>> " + year)

    return day, month, year


def display_dob(day, month, year):
    print(day, month, year, sep="-")
    return day, month, year


def main():
    day, month, year = get_dob()
    display_dob(day, month, year)


main()

