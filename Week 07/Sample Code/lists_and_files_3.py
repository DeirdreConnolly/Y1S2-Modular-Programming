'''
Reading numbers from a file into a list.
Method: Read a line at a time from the file, if nothing is read from the file, then the end of the file has been reached.
If something has been read from the file, convert it to an integer and append to a list.
'''
def main():
    data_file = open("numbers.txt")
    numbers = []
    while True:
        line = data_file.readline()
        if line == "":
            break
        numbers.append(int(line))
    data_file.close()
    print(numbers)


main()