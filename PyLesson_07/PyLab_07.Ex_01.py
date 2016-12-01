number = int(input("Please enter a number:"))
summ = 0
num = number

def sumDigits(num):
    global summ
    while num > 0:
        summ += num%10
        num = int(num / 10)

sumDigits(num)
        
print("The sum of the digits in", num, "is", summ)

    




