import math

class Time:
    def __init__(self, time):
        self.seconds = (int(time[1])*10 + int(time[2]))*3600 + (int(time[3])*10 + int(time[4]))*60

    def getTime(self):
        day = math.floor(self.seconds / 86400)
        if day == 1:
            return self.getHour() + ":" + self.getMinute() + " " + str(day) + " day after"
        elif day > 1:
            return self.getHour() + ":" + self.getMinute() + " " + str(day) + " days after"
        else:
            return self.getHour() + ":" + self.getMinute()

    def getHour(self):
        H = str(math.floor((self.seconds / 3600) % 24))
        if H.__len__() == 2:
            return H
        else:
            return "0" + H

    def getMinute(self):
        return str(int(self.seconds % 3600 / 60))


banana = Time("02535")
print(banana.getHour(), banana.getMinute(), banana.getTime())