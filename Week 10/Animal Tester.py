from Animal import Animal


def main():
    print("Tester for Animal class")
    animal1 = Animal("Barry", "dog", 2)
    animal2 = Animal("Larry", "cat", 3)
    animal3 = Animal("Garry", "mouse", 4)
    animal1.print_details()
    animal2.print_details()
    animal3.print_details()

    my_animals = [animal1, animal2, animal3]
    for item in my_animals:
        item.print_details()

    animal1.set_age(7)
    age = animal1.get_age()
    print("Animal1 new age is " + str(age))

    old_age = animal2.get_age()
    new_age = old_age + 1
    print("Animal2 new age is " + str(new_age))

main()



