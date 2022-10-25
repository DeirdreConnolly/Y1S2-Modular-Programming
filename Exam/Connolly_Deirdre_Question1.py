# Name:         Deirdre Connolly
# Student ID:   R00112962


def get_personal_info():
    name = input("Enter your name >>> ").upper()
    year_of_birth = input("Enter your year of birth >>> ")

    return name, year_of_birth


def generate_short_name(name, year_of_birth):                               # Fix this
    name_list = [name]
    short_name_list = []

    for name in name_list:
        short_name_list.append(name[0:3])                                   # .append(year_of_birth) ?

    print("Generated username >>> " + str(short_name_list).rstrip() + year_of_birth) # How to get rid of [''] in result?

    return short_name_list


def main():
    name, year_of_birth = get_personal_info()
    generate_short_name(name, year_of_birth)


main()
