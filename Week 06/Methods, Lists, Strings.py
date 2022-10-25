def target_times(time_taken, names):
    # print(time_taken[0], names[0])
    print("NAME", "TARGET TIME")
    target_time = [i * .9 for i in time_taken]
    i = 0
    for names in names:
        print(names, format(target_time[i], ".2f"))
        i = i + 1

def main():
    time_taken = [32, 27, 23, 26, 26, 18]
    names = ["Ann", "Joe", "Pat", "Ken", "Ali", "Ger"]
    target_times(time_taken, names)

main()

