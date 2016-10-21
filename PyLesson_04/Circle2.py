radius = int(input("What is the radius:"))
area = 0

def areaNums():
    global radius
    radius = radius

def multiplyNums():
    global area
    area = 3.14 * (radius**2)

areaNums()
multiplyNums()

print("The area of a circle with a radius of", (radius), "is", (area))
