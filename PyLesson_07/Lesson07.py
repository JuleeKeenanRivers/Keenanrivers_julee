number = int(input("Enter a number:"))
digits = 0
num = number 


while number > 0:
    digits += 1
    number = int(number/10)

print("There are", digits, "digits in", num)




