peopleInfo = {}
Alluser = []

print("\n\t*****PROGRAMMED BY*****")
print("\t***BATURIANO, JOSEPH Z.***")
print("\t******BSCOE 2-2******\n")


def menu():

    print("\n\t=========MENU=========")
    print("\n\t1 -> Add an item\n"
          "\n\t2 -> Search\n"
          "\n\t3 -> View all contacts\n"
          "\n\t4 -> Exit (y/n)")
    print("\n\t======================")


menu()


def add():
    peopleInfo = {}
    Nameval = input("\tEnter your Fullname: ").capitalize()
    Addressval = input("\tEnter your Address: ").capitalize()
    Ageval = int(input("\tEnter your age: "))
    Phone_noVal = int(input("\tEnter your phone number: "))
    bloodTypeval = input("\tEnter your Blood Type: ").upper()
    peopleInfo["Name"] = Nameval
    peopleInfo["Address"] = Addressval
    peopleInfo["Age"] = Ageval
    peopleInfo["Phone_number"] = Phone_noVal
    peopleInfo["BloodType"] = bloodTypeval
    Alluser.append(peopleInfo)
    print("<<<<<<<<<<<Information Saved!>>>>>>>>>>>")


def search():
    search = input("\tEnter your Full name: ").capitalize()
    for i in range(len(Alluser)):
        peopleInfo = Alluser[i]
        keys_ls = []
        for key, val in peopleInfo.items():
            keys_ls.append(key)
        for j in range(len(keys_ls)):
            key = keys_ls[j]
            if search == peopleInfo[key]:
                print("\nHere are the information of", search)
                print("\nFull Name:", search)
                print("Address: ", peopleInfo["Address"])
                print("Age: ", peopleInfo["Age"])
                print("Phone Number: ", peopleInfo["Phone_number"])
                print("Blood Type: ", peopleInfo["BloodType"])


def display_all():
    print("\n\tHERE ARE THE CONTACTS")
    for i in range(len(Alluser)):
        show = Alluser[i]
        print("\n\tFullname: ", show["Name"])
        print("\tAddress: ", show["Address"])
        print("\tAge: ", show["Age"])
        print("\tPhone number: ", show["Phone_number"])
        print("\tBlood Type: ", show["BloodType"])


# Allow user to select item in the menu (check if valid)
choice = int(input("\nEnter a choice from menu: "))
# Perform the selected option
ans = "y"
while ans == "y":
    if choice == 1:
        add()
        menu()
        choice = int(input("\nEnter a choice from menu: "))
    if choice == 2:
        search()
        menu()
        choice = int(input("\nEnter a choice from menu: "))
    if choice == 3:
        display_all()
        ans = input("\nGo back to menu(y/n): ")
        if ans == "y":
            menu()
            choice = int(input("\nEnter a choice from menu: "))
        else:
            break
    if choice == 4:
        leave = input(
            "\n\tAre you sure you want to leave this program?(y/n): ").lower()
        if leave == "n":
            menu()
            choice = int(input("\nEnter a choice from menu: "))
        else:
            print(
                "\n===========Thanks for using this program! Have a nice day!=============")
            break
