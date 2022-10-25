countries = {"France": [67, "French", "Paris"],
             "Italy": [63, "Italian", "Rome"],
             "Germany": [83, "Italian", "Rome"]
             }

for country,info in countries.items():
   print(country + ": Pop is " + str(info[0]) + "m. Capital is " + info[2] + ".")

biggestCountry = ""
max = 0
for country,info in countries.items():
    if info[0] > max:
        max = info[0]
        biggestCountry = country
print("The biggest country is "+ biggestCountry)


