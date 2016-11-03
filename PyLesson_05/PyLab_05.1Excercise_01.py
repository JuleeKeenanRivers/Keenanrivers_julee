science = input("enter grade for science class: ")
math = input("enter grade for math class: ")
english = input("enter grade for english class: ")
history = input("enter grade for history class: ")
spanish = input("enter grade for spanish class: ")
computerprogramming = input("enter grade for computerprogramming class: ")
cooking = input("what is your grade for spanish class: ")



def calcPoints(grade):
    if grade == "A":
        return 4.0
    elif grade == "B":
        return 3.0
    elif grade == "C":
        return 2.0
    elif grade == "D":
        return 1.0
    else:
        return 0.0
    
gradePoints = calcPoints(science) + calPoints(math) + calcPoints(english) + calcPoints(history) + calcPoints(spanish) + calcPoints(computerprogramming) + calcPoints(cooking)

print("Your GPA is", (gradePoints)/7)




    



