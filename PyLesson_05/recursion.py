

def recursion():
    choice = input("Would you like to do some recursion?")
    if choice == "Y" or choice == "N":
        if choice == "y":
            print("Yay! lets do some recursion!")
        else:
            print("spoiled the fun!")
    else:
        print("Please enter Y or N")
        recursion()

recursion()

