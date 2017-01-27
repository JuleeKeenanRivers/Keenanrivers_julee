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

    Human1 = human(hair, eyes, skin)

    print("My Info:")
    print("my hair:", Human1.getHair())
    print("my eyes:", Human1.getEyes())
    print("my skin:", Human1.getSkin())



    #modifier
    def setFHES(self, newh, newe, news):
        self.newhair = h
        self.neweyes = e
        self.newskin = s

    #accessors
        

    def getnewHair(self):
        return self.newhair

    def getnewEyes(self):
        return self.neweyes

    def getnewSkin(self):
        return self.newSkin

    newhair = input("hair:")
    neweyes = input("eyes:")
    newskin = input("skin:") 

    Human2 = human(newhair, neweyes, newskin)

    print("Friends Info:")
    print("friends hair:", Human2.getnewHair())
    print("friends eyes:", Human2.getnewEyes())
    print("friends skin:", Human2.getnewSkin())

main() 


        
