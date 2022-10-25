'''
Reading numbers from a file into a list.
Method: reads the contents into a list of strings using readlines() then converts into entry into an integer
'''
def main():
    data_file = open("numbers.txt")
    numbers_as_strings = data_file.readlines()
    print(numbers_as_strings)
    numbers = []
    for i in range(len(numbers_as_strings)):
        numbers.append(int(numbers_as_strings[i]))
    data_file.close()
    print(numbers)
main()