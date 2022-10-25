#   Name: 06_tuples.py
#   Demo of tuples and built in functions and methods
my_tuple = (5, 1, 2, 3)
print(my_tuple[0])
print("my tuple:")
for num in my_tuple:
    print(num)
new_tuple = my_tuple[0:2]
if  5 in  my_tuple:
    print("contains a 5")
num_of_items = len(my_tuple)
min = min(my_tuple)
max = max(my_tuple)
print("contains " + str(num_of_items) + " items")
pos = my_tuple.index(2)
print("contains a 2 at pos " + str(pos))
color_list = ["red", "green", "blue"]
color_tuple = tuple(color_list)
list_nums = list(my_tuple)
print("Tuple: ", color_tuple)
print("List: ", list_nums)
# my_tuple[0] = 5