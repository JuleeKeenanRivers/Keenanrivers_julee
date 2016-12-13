number = int(input("Please enter a number:"))
digits = 0
average = 0



def averageDigits(number):
    num = number
    global average, digits
    while num > 0:
        digits += 1
        average += num % 10
        num = int(num/10)
    average /= digits

averageDigits(number)

print("The average of the digits in", number, "is", average)








        
    

