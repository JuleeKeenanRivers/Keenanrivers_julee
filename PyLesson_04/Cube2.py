side = int(input("What is the length of the side:"))
sa = 0

def saNums():
    global side
    side = side

def multiplyNums():
    global sa
    sa = 6 *(side**2)

saNums()
multiplyNums()

print(" The surface area of a cube whose sides are", (side), "in length is", (sa))
