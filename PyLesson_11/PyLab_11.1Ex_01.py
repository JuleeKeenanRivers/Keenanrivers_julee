class car:
    #constructor
    def __init__(self, p, i, e, t):
        self.paint = p
        self.interior = i
        self.engine = e
        self.tires = t

    #modifier
    def setValues(self, p, i, e, t):
        self.paint = p
        self.interior = i
        self.engine = e
        self.tires = t

    #accessors

    def getPaint(self):
        return self.paint

    def getInterior(self):
        return self.interior

    def getEngine(self):
        return self.engine

    def getTires(self):
        return self.tires

def main():
    paint = input("Please enter a paint color:")
    interior = input("Please choose an interior:")
    engine = input("please enter an engine type:")
    tires = input("Please enter type of tires:")

    #instantate an object

    Car1 = car(paint, interior, engine, tires)

    print("Your Car is ready:")
    print("Paint:",Car1.getPaint())
    print("interior:",Car1.getInterior())
    print("engine:",Car1.getEngine())
    print("Tires:",Car1.getTires())

main() 

    

    
        
        
        
        
        
        
