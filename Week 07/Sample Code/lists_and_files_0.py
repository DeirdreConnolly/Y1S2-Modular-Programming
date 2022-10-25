'''
Reading numbers from a file into a list.
Method: reads the contents into a list of strings using readlines() then converts into entry into an integer
'''
def main():
    names = ["Mary", "Ann", "Ben", "Kate", "Emily"]
    ages = [4, 7, 9, 2, 1]
    data_file = open("output.txt", "w")

    for i in range(len(ages)):
        data_file.write(names[i] + " is " + str(ages[i]) + " years old.\n")

    data_file.close()

main()