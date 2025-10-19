CountryCapital = {"USA":"Washington DC","India":"New Delhi","Nigeria":"Abuja","France":"Paris","UK":"London","Japan":"Tokyo"}
while True:
    print("Welcome to World Country Capitals Database Game!")
    print("1. Add Countries")
    print("2. View Countries")
    print("3. View Capitals")
    print("4. View All")
    print("5. Extract Capital")
    print("6. Delete Country")
    print("7. Exit")

    choice = int(input("Enter your choice"))
    if choice == 1:
        choiceofcountry = input("Enter a country")
        if choiceofcountry in CountryCapital:
            print("Country already exists within database, try again.")
            choiceofcountry = input("Enter a different country")
        choiceofcapital = input ("Enter the capital")
        CountryCapital [choiceofcountry] = choiceofcapital
        print("Country Added.")

    elif choice == 2:
        print("The countries availible are" , CountryCapital.keys())

    elif choice == 3:
        print("The capitals availible are" , CountryCapital.values())

    elif choice == 4:
        print("All the countries and capitals are:" , CountryCapital)

    elif choice == 5:
        extractcountry = input("Which country would you like to know the capital of?")
        if extractcountry not in CountryCapital:
            print("This country doesn't exist within the database, retry")
            extractcountry = input("Enter the country you would like to know the capital of again")
        elif extractcountry in CountryCapital:
            print(CountryCapital[extractcountry])

    elif choice == 6:
        deletechoice = input("Which country would you like to remove?")
        if deletechoice not in CountryCapital:
            print("You cannot delete this country as it doesn't exist within the database, retry!")
            deletechoice = input("Re-enter the country you want to remove")
        elif deletechoice in CountryCapital:
            del CountryCapital [deletechoice]

    elif choice == 7:
        print("Bye! Thanks for playing!")
        break






        