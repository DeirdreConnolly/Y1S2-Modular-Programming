# Author:       Deirdre Connolly
# Filename:     Homework.py
# Description:  Practice exercises


# Q1+2
def countdown():
    count_start = int(input("Countdown starts at: "))
    count_end = int(input("Countdown ends at: "))
    i = count_start + 1
    while i > count_end:
        i = i - 1
        print(i)

    if count_end == 1:
        print("Blast Off!")

    elif count_end != 1:
        print("Mission Aborted")

countdown()



