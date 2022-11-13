peopleInfo = {}
Alluser = []

print("\n\t*****PROGRAMMED BY*****")
print("\t***BATURIANO, JOSEPH Z.***")
print("\t******BSCOE 2-2******\n")


def menu():

    print("\n\t=========MENU=========")
    print("\n\t1 ---> Add an item\n"
          "\n\t2 ---> Search\n"
          "\n\t3 ---> View all contacts\n"
          "\n\t4 ---> Exit (y/n)")
    print("\n\t======================")


menu()


def add():
    peopleInfo = {}
    Nameval = input("\n\tEnter your Fullname: ").capitalize()
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
    print("\n<<<<<<<<<<<Information Saved!>>>>>>>>>>>")


def search():
    search = input("\n\tEnter your Full name: ").capitalize()
    for i in range(len(Alluser)):
        peopleInfo = Alluser[i]
        keys_ls = []
        for key, val in peopleInfo.items():
            keys_ls.append(key)
        for j in range(len(keys_ls)):
            key = keys_ls[j]
            if search == peopleInfo[key]:
                print("\t\n<<<<<<<<<<<<This is the information of",
                      search, ">>>>>>>>>>>>>>>>>>\n")
                print("\n\tFull Name:", search)
                print("\tAddress: ", peopleInfo["Address"])
                print("\tAge: ", peopleInfo["Age"])
                print("\tPhone Number: ", peopleInfo["Phone_number"])
                print("\tBlood Type: ", peopleInfo["BloodType"])


# Allow user to select item in the menu (check if valid)
choice = int(input("\nEnter a choice from menu: "))
# Perform the selected option
while True:
    if choice == 1:
        add()
        menu()
        choice = int(input("\nEnter a choice from menu: "))
    if choice == 2:
        search()
        menu()
        choice = int(input("\nEnter a choice from menu: "))
