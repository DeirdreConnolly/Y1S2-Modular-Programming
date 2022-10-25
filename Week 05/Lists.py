# Q1
list1 = [1,2,3,4]
print(list1)

print(list1[0])

print(list1[-1])

print(len(list1))

list2 = [] + list1

i = 0
while i < len(list1):
    print(str(i) + " " +  str(list1[i]))
    i = i + 1

for item in list1:
    i = i + 1
    print(item, end="\t")

for item in list2:
    i = i + 1
    print(item, end="\t")


# Q2
print("\n")
list3 = [8,8,8,9,9,9]
print(list3)
list3[4:6] = [0,0]
print(list3)
list3.reverse()
print(list3)
print(list3[:])

total = sum(list3)
print("Total = " + str(total))


# Q3
countries = ["Spain", "Brazil", "Portugal", "Bolivia"]
print(countries)

countries.append("Italy")
print(countries)

countries.remove("Bolivia")
print(countries)

group1 = countries[0:2]
print(group1)
group2 = countries[2:6]
print(group2)

