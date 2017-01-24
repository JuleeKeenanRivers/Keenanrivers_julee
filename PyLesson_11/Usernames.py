class UserNames:
    #constructor
    def __init__(self, fName,lName,uName):
        self.firstName = fName
        self.lastName = lName
        self.userName = uName

    #Modifier
    def setUserName(self, newUser):
        self.userName = newUser

    #Accessors
    def getFirstName(self):
        return self.firstName

    def getLastName(self):
        return self.lastName

    def getUserName(self):
        return self.userName

def main():
    firstName = input("Please enter your first name:")
    lastName = input("Enter your last name:")
    userName = input("enter your desired user name:")

    #instantate an object

    user1 = UserNames(firstName, lastName, userName)

    print("<<<<< USER INFO>>>>>>")
    print("Name:", user1.getFirstName()," ", user1.getLastName())
    print("User Name:", user1.getUserName(), "\n\n")


main() 
