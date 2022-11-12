peopleInfo = {}
print("\n\t*****PROGRAMMED BY*****")
print("\t***BATURIANO, JOSEPH Z.***")
print("\t******BSCOE 2-2******\n")


def menu():

    print("\n\t=========MENU=========")
    print("\n\t1 -> Add an item\n"
          "\n\t2 -> Search\n"
          "\n\t3 -> Exit (y/n)")
    print("\n\t======================")


menu()


def add():
    Name = input("\tEnter your Full name: ").capitalize()
    Address = str(input("\tEnter your address: ")).capitalize()
    peopleInfo[Name] = Address
    Age = input("\tEnter your age: ")
    peopleInfo[Name] = Age
    Phone_no = int(input("\tEnter your phone number: "))
    peopleInfo[Name] = Phone_no
    bloodType = input("\tEnter your Blood Type: ")
    peopleInfo[Name] = bloodType
    print("Information Saved!")


# Allow user to select item in the menu (check if valid)
choice = int(input("Enter a choice from menu: "))
# Perform the selected option
while True:
    if choice == 1:
        add()
        menu()
