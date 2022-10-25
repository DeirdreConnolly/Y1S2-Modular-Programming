def get_months_beginning_with(months, letter):
    list1 = []
    for month in months:
        if month.startswith(letter):
            list1.append(month)
    return list1


def get_short_names(months, letter):
    list2 = []
    for month in months:
        if month.startswith(letter):
            list2.append(month[0:3])
    return list2


months = [ "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

j_months = get_months_beginning_with(months, "J")
print(j_months)

j_months_short = get_short_names(months, "J")
print(j_months_short)