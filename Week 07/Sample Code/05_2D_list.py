names = [["Andy", "Amy", "Alice", "Alan"], ["Ber", "Billy", "Ben", "Bert"], ["Cath", "Cindy", "Clare", "Con"]]
# We can visualise this a
#  set of  rows of info
#   Col:      0        1       2         3
#  Row 0    "Andy"  "Amy"    "Alice"  "Alan"
#  Row 1    "Ber"   "Billy"  "Ben"    "Bert"
#  Row 2    "Cath"  "Cindy"  "Clare"  "con"
#  To print 1 item we need 2 subscripts
#  To print one of all the item in ( row 0)
#  [0][0]
#  [0][1]
#  [0][2]
#  [0][3]
print("Row 0: ", names[0][0], names[0][1], names[0][2], names[0][3])
#  To print one of all the items in list 1 ( row 1)
print("Row 1: ", names[1][0], names[1][1], names[1][2], names[1][3])
#  To print one of all the item in list 1 ( row 2)
print("Row 2: ", names[2][0], names[2][1], names[2][2], names[2][3])

# To print all the items in teh firs column
print("Column 0:")
print(names[0][0])
print(names[1][0])
print(names[2][0])

# To print out all items in a loop
# print  in a loop by  1 row at a time
print("Print each row 1 at a time")
ROWS= 3
COLUMNS = 4
for r in range(ROWS):
    for c in range(COLUMNS):
        print(names[r][c])
    print("-------")

print("Print each column 1 at a time")
for c in range(COLUMNS):
    for r in range(ROWS):
            print(names[r][c])
    print("-------")
