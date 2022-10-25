'''
Reading data from a file into 2 lists.
The format of the file has now changed so that the name and age are on the same line.
Method: Read a line from the file, if nothing was read then we have reached the end of the file.
If something has been read, then split that line to a list consisting of 2 items - the name at index 0 and the age at
index 1.
'''
def main():
    data_file = open("numbers_and_names_one_line.txt")
    names = []
    ages = []
    while True:
        line = data_file.readline()
        if line == "":
            break
        line_list = line.split()
        names.append(line_list[0])
        ages.append(int(line_list[1]))
    data_file.close()
    print(names)
    print(ages)


main()