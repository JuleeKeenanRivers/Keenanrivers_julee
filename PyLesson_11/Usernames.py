class Usernames:
    #constructor
    def __init__(self, fName,lName,uName):
        self.firsName = fName
        self.lastName = lName
        self.userName = uName

    #Modifier
    def setUName(self, newUser):
        self.userName = newUser

    #Accessors
    def getFirstName(self):
        return self.firsName

    def getLastName(self):
        return self.lastName

    def getUserName(self):
        return self.username

    def main():
        firstName = input("Please enter your first name:")
        lastName = input("Enter your last name:")
        userName = input("enter your desired user name:")

        user1 = user_Account(firstName, lastName, userName)

        print("<<<<< USER INFO>>>>>>")
        print("Name:", user1.getFirstName()," ", user1.getLastName())
        print("User Name:", user1.getUserName(), "\n\n")

        user1.setUName("pHandsome")

        print("<<<<< USER INFO>>>>")
        print("Name:", user1.getFirstName(), " ", user1.getLastName())
        print("User Name:", user1.getUserName(), "\n\n")

    main() 
