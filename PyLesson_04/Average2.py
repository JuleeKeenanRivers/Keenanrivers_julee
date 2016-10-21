num1 = int(input("What is the first number:"))
num2 = int(input("What is the second number:"))
num3 = int(input("What is the third number:"))
avg = 0

def avgNums():
    global num1, num2, num3
    num1 = num1
    num2 = num2
    num3 = num3

def multiplyNums():
    global avg
    avg = (num1 + num2 + num3)/(3)

avgNums()
multiplyNums()

print("The average of,", (num1),"," ,(num2), ",and", (num3), "is", (avg))


