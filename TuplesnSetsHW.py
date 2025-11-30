patients = ("Ava","Bob","Charlie","Diana","Eden","Flora","Gemma","Harrison","Iliya","Josh","Kieron","Leah","Mary","Nara","Owen","Priya")
fluPatients = {"Ava","Bob", "Flora", "Josh", "Charlie","Eden","Gemma","Iliya","Kieron","Mary","Owen"}
coldPatients = {"Bob","Diana","Flora","Harrison","Josh","Leah","Nara","Priya","Eden", "Iliya"}

while True:
    print("Welcome to your first shift at the Hospital of Jetlearn")
    print("Would you like to...")
    print("1. See the names of your patients")
    print("2. See how many patients you have")
    print("3. See your first 3 patients")
    print("4. See what patients have only a cold")
    print("5. See what patients have only the flu")
    print("6. See what patients have both the cold and a flu")
    print("7. Finish your shift")

    choice = input("What is your choice?")
    if choice == "1":
        print(patients)
    
    elif choice == "2":
        print(len(patients))
    
    elif choice == "3":
        print(patients[0:3])
    
    elif choice == "4":
        print(coldPatients.difference(fluPatients))
    
    elif choice == "5":
        print(fluPatients.difference(coldPatients))
    
    elif choice == "6":
        print(fluPatients.intersection(coldPatients))
    
    elif choice == "7":
        print("Thanks for working today!")
        print("Clocking out...")
        break

