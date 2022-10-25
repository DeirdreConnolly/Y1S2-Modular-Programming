# Name:         Deirdre Connolly
# Student ID:   R00112962


line = ("-"*20)

days_list = ["Monday\t", "Tuesday\t", "Wednesday", "Thursday", "Friday\t"]
ice_cream_sold = [105, 44, 22, 121, 17]

print("DAY", "PROFITS", sep="\t"*3)
print(line)

length = len(days_list)
i = 0
while i < length:
    print(days_list[i], ice_cream_sold[i], sep="\t"*1)
    i = i + 1


# FIX THIS
#if int(ice_cream_sold) > 50:
#    ice_cream_sold.append("*")

#for item in ice_cream_sold:
#    if int(item) > 50:
#        ice_cream_sold.append("*")


print(line)


# HIGHEST SALES
highest = max(ice_cream_sold)

i = 0
for item in ice_cream_sold:
    if item == highest:
        print("The highest sales were " + str(highest) + " sold on " + days_list[i] + ".")
    i = i + 1