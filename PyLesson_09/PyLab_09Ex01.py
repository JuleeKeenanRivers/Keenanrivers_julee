newList = ["hello", "hey", "hi", "hola", "heyy"]

print("In order...")


for wd in newList:
    print(wd)
print("")

print("Reversed....")

def reverse(array):
    for i in range(len(array)-1,0,-1):
        print(newList[i])

reverse(newList)

    
    

