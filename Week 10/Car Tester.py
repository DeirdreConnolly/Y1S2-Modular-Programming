from Car import Car


def main():
    make = input("Enter make of car >>> ")
    model = input("Enter model of car >>> ")
    year = int(input("Enter year of car >>> "))

    print("Here is the data that you entered:" )

    car1 = Car(make, model, year)
    car1.print_details()


main()
