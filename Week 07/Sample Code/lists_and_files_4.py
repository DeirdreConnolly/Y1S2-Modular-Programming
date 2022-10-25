'''
Reading strings and integers from a file.
Method: Read a line at a time from the file, if nothing is read from the file, then the end of the file has been reached.
If something has been read from the file, append it to a names list then get the next line from the file and
convert it to an integer and append to an integer list.

Assumption: The format of the file is name followed by number (age).
'''
def main():
    data_file = open("numbers_and_names.txt")
    names = []
    ages = []
    while True:
        line = data_file.readline().rstrip()
        if line == "":
            break
        names.append(line)
        line = data_file.readline().rstrip()
        ages.append(int(line))
    data_file.close()
    print(names)
    print(ages)


main()