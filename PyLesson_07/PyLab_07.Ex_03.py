number = int(input("Please enter a number:"))
num = number
rev = 0

def getReverse(num):
    global rev 
    while num > 0:
        rev *= 10
        print(number%10) 
        num = int(num/10)
        rev = num
       
getReverse(num)

print(number , "reversed is" , rev)




