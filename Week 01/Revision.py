# Author: Deirdre
# File Name: Revision.py
# Description: Revision questions

heading = ("Name" + "\t\t" + "Result" + "\t\t" + "Grade")
newFile = open("Results.txt", "w")
newFile.write(heading)

numOfStudents = int(input("Enter number of students: "))

i = 0
while i < numOfStudents:
    i = i + 1
    valid = False
    while valid is False:
        name = input("Enter name: ")
        length = len(name)

        if length < 2:
            print("Invalid input, please try again.")
        else:
            valid = True

    valid = False
    while valid is False:
        result = int(input("Exam result: "))

        if result < 0 or result > 100:
            print("Invalid input, please try again.")
        else:
            valid = True

        if 70 <= result <= 100:
            grade = "H1"
        elif 60 <= result <= 69:
            grade = "H21"
        elif 50 <= result <= 59:
            grade = "H22"
        elif 40 <= result <= 49:
            grade = "Pass"
        elif 0 <= result <= 39:
            grade = "Fail"
        else:
            print("Invalid format.")

        newFile.write("\n" + name + "\t\t" + str(result) + "\t\t\t" + grade)

        total = 0 + result

average = (total/ numOfStudents)
newFile.write("\n\n" + "Average: \t" + str(average))

newFile.close()

