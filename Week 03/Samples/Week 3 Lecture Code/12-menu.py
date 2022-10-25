# global constants
COFFEE = 2.20
TEA = 1.70
MILK = 1.65

# function to validate that x lies between
# minimum and maximum inclusive
# This function can now be added to many applications
# in which we need to check the range
def check_if_valid(minimum, maximum, x):
    return minimum <= x <= maximum


# function to get the user's drink choice
def get_choice():
    menu = "Would you like " + "\n\t1: Coffee" \
                               "\n\t2: Tea" \
                               "\n\t3: Milk" \
                               "\n\t4: Quit" \
                               "\n==> "
    something_is_wrong = True
    while something_is_wrong:
        try:
            number = int(input(menu))
            if check_if_valid(1,4, number):
                something_is_wrong = False
            else:
                print("Values 1-4 please...")
        except:
            print("Must be numeric...")
    return number

# function to save me having to write the format()
# statement for currency each time I need it.
def tidy_money(money):
    return format(money, '.2f')


def process_choice(choice):
    if choice == 1:
        cost = COFFEE
    elif choice == 2:
        cost = TEA
    elif choice == 3:
        cost = MILK
    print("That will be €" + tidy_money(cost))


def main():
    while True:
        users_choice = get_choice()
        if users_choice == 4:
            break
        process_choice(users_choice)


main()