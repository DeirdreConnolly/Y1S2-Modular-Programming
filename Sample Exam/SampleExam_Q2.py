# File Name:    SampleExam_Q2.py
# Author:       Deirdre Connolly
# Description:  Q2

lecturers = ["Mickey Mouse", "Daisy Duck    ", "Yosemite Sam", "Speedy Gonzalez", "Lola Bunny   "]
attendances = [56, 63, 57, 63, 61]

sep = "\t"*2
line = "-"*26
print("LECTURER" + sep + "ATTENDANCE")
print(line)

amount = len(lecturers)
i = 0
while i < amount:
    print(lecturers[i], attendances[i], sep="\t"*2)
    i = i + 1

print(line)


# MOST POPULAR TEACHER
highest = max(attendances)

print("Max Attendance" + sep + str(highest))

i = 0
for item in attendances:
    if item == highest:
        print(lecturers[i])
    i = i + 1