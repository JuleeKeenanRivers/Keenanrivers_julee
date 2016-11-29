number = int(input("Please enter a number:"))
num = number
sum = 0

def sumDigits(num):
    global sum
    while num > 0:
        sum += num%10
        num = int(num /= 10)

sumDigits(num)
        
print("The sum of the digits in", num, "is", sum)

    



