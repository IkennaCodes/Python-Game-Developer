#Sets (groups)
cooking = {"Adanna", "Ikenna", "Charlie", "Renuka", "Sara", "Bob", "Sienna", "Gary"}
reading = {"Charlie", "Sara", "Sienna", "Bob", "Renuka", "Millie", "Ivana"}

#Names of all
print(cooking.union(reading))

#Names who like both
print(cooking.intersection(reading))

#Names who like cooking but not reading
print(cooking.difference(reading))

#Names who like reading but not cooking
print(reading.difference(cooking))

