dictionary = {"car":"A road vehicle with an engine, wheels and seats used for transportation and to travel","ball":"a round object used in games or sports","tree":"a tall plant with a wooden trunk, branches and leaves","fish":"an animal that lives in water and breathes through gills","cup":"a small container used for holding and drinking liquids","door":"a movable barrier used to open or close and entrance","book":"a set of written or printed pages bound together"}
while True:
    print("Welcome to the Dictionary!")
    print("1. View Dictionary")
    print("2. Search for a word")
    print("3. Add a word")
    print("4. Delete a word")
    print("5. Check how many words")
    print("6. Exit")

    choice = int(input("Enter a number from 1-6"))

    if choice == 1:
        print("Here are our words in the dictionary!")
        print(dictionary)

    elif choice == 2:
        search = input("Enter the word you are searching for")
        if search not in dictionary:
            input("Error, Re-Enter a word that's in dictionary")
        else:
            print(dictionary[search])

    elif choice == 3:
        addingword = input("Enter the word you want to add")
        if addingword in dictionary:
            input("Error, word already in dictionary, re-enter")
        else:
            addingdef = input("Enter the definition")
            dictionary [addingword] = [addingdef]
            print("Word has been added!")
            print(dictionary)

    elif choice == 4:
        delword = input("Enter the word you want to delete")
        if delword not in dictionary:
            input("Error, word not in dictionary, re-enter")
        else:
            del dictionary [delword]
            print(dictionary)

    elif choice == 5:
        print(len(dictionary))

    elif choice == 6:
        print("Thanks for browsing the dictionary today!")
        break



