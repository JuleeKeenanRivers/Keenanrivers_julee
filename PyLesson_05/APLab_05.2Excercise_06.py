user = "juleekr"
passw = "password"
username = input("Enter your username here:")
password = input("Enter your password here:")

def passCheck():
    if username == "juleekr" and password == "password":
        print("Access granted!")
    elif username == "juleekr" and password != "password":
        print("Wrong password")
    elif username != "juleekr" and password == "password":
        print("Wrong password")
    else:
        print("wrong password and username")
passCheck() 

