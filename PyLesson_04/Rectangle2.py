length = int(input("What is the length:"))
width = int(input("What is the width:"))
perimeter = 0

def perimeterNums():
    global length, width
    length = length
    width = width 

def multiplyNums():
    global perimeter
    perimeter = 2*(length) + 2*(width)

perimeterNums()
multiplyNums()

print("Your rectangle is", (perimeter), "ft around")

