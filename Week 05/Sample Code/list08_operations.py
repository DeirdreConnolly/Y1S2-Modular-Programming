#   Name: list operations
#   Desc:  operations on lists
#   Author: Helen Fagan
results = [80, 55, 67, 91,45]
results.append(40)
results.remove(55)
results.sort()
results.reverse()
index1 = results.index(91)
index2 = results.index(67)
print(results)
print(index1)
print(index2)
item1 = results.pop()
item2 = results.pop(2)
item3 = results.pop(-1)
print(str(item1) + " "  + str(item2) + " " + str(item3))
print(results.count(45))
print(results)
print(min(results))