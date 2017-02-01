class Human:
    #constructor
    def __init__(self, h, e, s):
        self.hair = h
        self.eyes = e
        self.skin = s

    #modifier
    def setHES(self, h, e, s):
            self.hair = h
            self.eyes = e
            self.skin = s

    #accessors

    def getHair(self):
            return self.hair

    def getEyes(self):
            return self.eyes

    def getSkin(self):
            return self.skin

def main():
    hair = input("Hair:")
    eyes = input("Eyes:")
    skin = input("skin:")

    #instantate an object

    human1 = Human(hair, eyes, skin)

    print("My Info:")
    print("my hair:", human1.getHair())
    print("my eyes:", human1.getEyes())
    print("my skin:", human1.getSkin())

    human1.setHES("blonde", "blue", "tan")

    print("Friends Info:")
    print("friends hair:", human1.getHair())
    print("friends eyes:", human1.getEyes())
    print("friends skin:", human1.getSkin())

main() 


        
