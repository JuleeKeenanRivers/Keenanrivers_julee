
class MilesPerHour:
    #constructor
    def __init__(self, dist = 0, ho = 0, mi = 0):
        self.distance = dist
        self.hours = ho
        self.minutes = mi
        mph = 0

    #modifer
    def setValues(self, dist, ho, mi):
        self.distance = dist
        self.hours = ho
        self.minutes = mi
        mph = 0
        

    #Accessors
    def getDistance(self):
        return self.distance

    def getHours(self):
        return self.hours

    def getMinutes(self):
        return self.minutes

    def getMPH(self):
        self.mph = float(self.distance)/((self.hours + self.minutes)/60.0)
        return self.mph 

def main():
    distance = int(input("please enter a distance:"))
    hours = int(input("please enter the hours:"))
    minutes = int(input("please enter minutes:"))

    #intstantate an object

    MPH1 = MilesPerHour()

    print("<<<<MPH information>>>>")
    print("Distance:", MPH1.getDistance(), "Hours:", MPH1.getHours())
    print("Minutes:", MPH1.getMinutes())

    MPH1.setValues(distance,hours,minutes)

    print("<<<<MPH information>>>>")
    print("Distance:", MPH1.getDistance(), "Hours:", MPH1.getHours())
    print("Minutes:", MPH1.getMinutes())
    print("mph: "+ str(MPH1.getMPH()))

main()
    
