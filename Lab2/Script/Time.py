import math

class Time:
    def __init__(self, time):
        self.seconds = (int(time[1])*10 + int(time[2]))*3600 + (int(time[3])*10 + int(time[4]))*60

    def intTime(self, hour, minutes):
        self.seconds = hour*3600 + minutes*60

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
        m = str(int(self.seconds % 3600 / 60))
        if len(m) == 2:
            return m
        else:
            return "0" + m

    def __lt__(self, other):
        return self.seconds < other.seconds

    def __gt__(self, other):
        return self.seconds > other.seconds

    def __ge__(self, other):
        return self.seconds >= other.seconds

    def __eq__(self, other):
        return self.seconds == other.seconds

    def __str__(self):
        return self.getTime()

    def __repr__(self):
        return self.getTime()

    def __hash__(self):
        return hash(self.seconds)

    def add_seconds(self, seconds):
        self.seconds += seconds


"""bananagrossa = Time("00000")
bananagrossa.seconds = 46800
print(bananagrossa.getHour(), bananagrossa.getMinute(), bananagrossa.getTime())
banana = Time("02535")
print(banana.getHour(), banana.getMinute(), banana.getTime())"""