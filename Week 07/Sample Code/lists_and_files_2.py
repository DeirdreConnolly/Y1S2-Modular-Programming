'''
Readings numbers from a file into a list.
Method: counts the number of lines in the file, then loops that many times, reading a line from the file and converting
it to an integer.
'''
def main():
    data_file = open("numbers.txt")
    number_of_numbers = len(data_file.readlines())
    numbers = []
    data_file.seek(0)
    for i in range(number_of_numbers):
        line = data_file.readline()
        numbers.append(int(line))
    data_file.close()
    print(numbers)


main()