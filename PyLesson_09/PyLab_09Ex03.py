import random
numbers = []

for i in range(0,10):
    numbers.append(random.randint(0,100))

output = ""
for value in numbers:
    output += str(value) + " "

print(output)

print("")

def average(LiSt):
    summ = 0
    for num in LiSt:
        summ += num
    return(summ/len(LiSt))


print("The average of the above numbers is..." + str(average(numbers)))



        
        




    
