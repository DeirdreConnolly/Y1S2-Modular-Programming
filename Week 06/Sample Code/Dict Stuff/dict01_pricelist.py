pricelist = {"Oranges": 45, "Apples":50, "Kiwis": 30}
print(pricelist.keys())
print(pricelist.values())
print(pricelist.items())
print(len(pricelist))
print(pricelist["Kiwis"])
pricelist["Oranges"] = 48
for key in pricelist.keys():
    print(key)
for price in pricelist.values():
    print(price)
for item in pricelist.items():
    print(item )
for k,v in pricelist.items():
    print(k + " " + str(v))
keysList = {k for k  in pricelist.keys() }
print(keysList)
