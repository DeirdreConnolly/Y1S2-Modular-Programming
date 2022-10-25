# Using parallel arrays for dance scores

scores = [9,8,6,7,6]
judges = ["Kim", "Tim", "Finn", "Lynn", "Wynn"]

total = sum(scores)
print("Total score:", total)

average = (total / len(scores))
print("Average score:", average)

min = min(scores)
print("Min score:", min)

max = max(scores)
print("Max score:", max)

i = 0
for item in scores:
    print(item, end="\t")
    if item == min:
        # print("found" + str(i))
        print(judges[i])
    i = i + 1

#a nswer = scores.index(9)
# print(" test" + str(answer))
# answer = scores.index(9, answer, 5)
# print(answer)
