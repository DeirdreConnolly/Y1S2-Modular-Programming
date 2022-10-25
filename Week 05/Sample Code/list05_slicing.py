#   Name; slicing
#   Desc: details of slicing
#   Author: Helen Fagan
days = [ "Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun"]
midweek= days[2:5]
print(midweek)
firstThreeDays = days[:3]
lastTwoDays = days[-2:]
print(firstThreeDays)
print(lastTwoDays)
all = days[:]
print(all)
endDays = days[5:19]
print(endDays)
everySecondDay = days[0:6:2]
print(everySecondDay)
empty = days[2:1]
print(empty)