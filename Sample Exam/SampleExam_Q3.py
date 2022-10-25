# File Name:    SampleExam_Q3.py
# Author:       Deirdre Connolly
# Description:  Q3


def read_attendances():
    file = open("yoga.txt")
    attendance = file.readlines()
    attendance_list = []
    for i in range(len(attendance)):
        attendance_list.append(int(attendance[i]))
    print(attendance_list)
    print("Total attendance: " + str(sum(attendance_list)))
    file.close()
    return attendance_list


def wages(read_attendances):
    attendance_list = read_attendances()
    wages = (sum(attendance_list) * 5.5)                                    # €5.50 per attendee
    print("Wages: €" + str(wages))


wages(read_attendances)