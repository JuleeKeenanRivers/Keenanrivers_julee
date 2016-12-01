def averageDigits(number):
    global average
    digits = 0
    base = 0
    num = number
    while num > 0:
        digits += 1
        base += digits%10
        num = int(num/10)
    average = base/digits

numbr = int(input("Please enter a number:"))
average = 0

averageDigits(numbr)

print("The average of the digits in", numbr, "is", average)


        
    
