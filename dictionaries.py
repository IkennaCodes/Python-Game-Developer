#Defining Items
bakery = {"bread":"£2","donut":"60p","cookie":"40p","chocolate":"£1","sandwich":"£1.50"}
print(bakery)

#Counting Items
print(len(bakery))

#Adding Items
bakery["croissant"] = "90p"
print(bakery)

#Deleting Items
del bakery ["donut"]
print(bakery)

#Changing Values
bakery["chocolate"] = "£1.20"
print(bakery)

#Print Keys Only
print(bakery.keys())

#Print Values Only
print(bakery.values())

#Print All
print(bakery.items())

#Using For Loop
for i in bakery.values():
    print (i)

for x in bakery.keys():
    print (x)
    
for a in bakery.items():
    print (a)