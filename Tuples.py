#this is a tuple, they are read only
colours = ("Red","Orange","Yellow","Green","Blue","Purple","White","Black")

print(colours)

#shows as tuple
print(type(colours))

#loop
for x in colours:
    print(x)   

#prints the number of items
print(len(colours))   

print(colours[0])

#shows as blue
print(colours[4])

#print first 3 colours
print(colours[0:3])

#green to white
print(colours[3:7])