countries = {"France": [67, "French", "Paris"],
             "Italy": [63, "Italian", "Rome"],
             "Germany": [83, "Italian", "Rome"]
             }
print("Pop  Italy")
country = countries.pop("Italy")
print(country)
print(len(countries))
print("Delete France")
del countries["France"]
print("Check remaining count")
print(len(countries))
print("Remove remaining countries")
countries.clear()
print("Check remaining count")
print(len(countries))

