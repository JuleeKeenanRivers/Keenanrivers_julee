class MilesPerHour:
    #constructor
    def __init__(self, dist, ho, mi):
        self.distance = dist
        self.hours = ho
        self.minutes = mi
        mph = 0

    #modifer
    def setValues(self, distance, hours, minutes):
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

def main():
    distance = input("please enter a distance:")
    hours = input("please enter the hours:")
    minutes = input("please enter minutes:")

    #intstantate an object

    MPH1 = MilesPerHour(distance, hours, minutes)

    print("<<<<MPH information>>>>")
    print("Distance:", MPH1.getDistance(), " ", MPH1.getHours())
    print("Minutes:", MPH1.getMinutes())

    MPH1.__init__()

main()
    
