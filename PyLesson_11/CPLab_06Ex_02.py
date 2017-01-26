import math

class distance:
    #constructor
    def __init__(self, x1 = 0, y1 = 0, x2 = 0, y2 = 0):
        self.xOne = x1
        self.yOne = y1
        self.xTwo = x2
        self.yTwo = y2
        self.distance = 0

    #Modifier
    def setValues(self, x1, y1, x2, y2):
        self.xOne = x1
        self.yOne = y1
        self.xTwo = x2
        self.yTwo = y2
        self.distance = 0

    #Accessors
    def getXOne(self):
        return self.xOne

    def getYOne(self):
        return self.yOne

    def getXTwo(self):
        return self.xTwo

    def getYTwo(self):
        return self.yTwo

    def getDistance(self):
        self.distance = float((self.xTwo-self.xOne)*(self.xTwo-self.xOne) + (self.yTwo-self.yOne)*(self.yTwo-self.yOne))
        return self.distance
    
def main():
    xOne = int(input("Please enter x1 coordinate:"))
    yOne = int(input("Please enter a y1 coordinate:"))
    xTwo = int(input("Please enter a x2 coordinate:"))
    yTwo = int(input("Please enter a y2 coordinate:"))

    #instantate an object

    D1 = distance(xOne, yOne, xTwo, yTwo) 

    print("<<<Distance information>>>")
    print("X1:", D1.getXOne(), "Y1:", D1.getYOne(), "X2:", D1.getXTwo(), "Y2:", D1.getYTwo())

    D1.setValues(xOne, yOne, xTwo, yTwo)

    print("<<<Distance information>>>")
    print("X1:", D1.getXOne(), "Y1:", D1.getYOne(), "X2:", D1.getXTwo(), "Y2:", D1.getYTwo())
    print("distance:" + str(D1.getDistance()))
    



main() 
        
