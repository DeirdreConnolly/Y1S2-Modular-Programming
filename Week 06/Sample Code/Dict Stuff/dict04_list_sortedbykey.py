countries = {"France": [67, "French", "Paris"],
             "Italy": [63, "Italian", "Rome"],
             "Germany": [83, "Italian", "Rome"]
             }

for country in sorted(countries.keys()):
    info = countries[country]
    print( country + "\t" + str(info[0]) + " m.")
