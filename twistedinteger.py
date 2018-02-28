from twistedint import *

class TwistedInteger:
    def __init__(self, n):
        self.size = n
        self.list = []
        for i in range(0, n-1):
            self.list.append(TwistedInt(i, n))

    def __str__(self):
        return str(self.list)

    def __repr__(self):
        return str(self.list)

    def Size(self):
        return self.size

    def IntegerList(self):
        return self.list

    def addTwoTwistedInt(self, first, second):
        if (not (0 < first < self.size)) or (not (0 < second < self.size)):
            message = "The value of the TwistedInt should be in range of (0 ~ "
            message += str((self.size - 1))
            message += ')'
            raise TypeError(message)
        else:
            return (self.list[first] + self.list[second])

    def mulTwoTwistedInt(self, first, second):
        if (not (0 < first < self.size)) or (not (0 < second < self.size)):
            message = "The value of the TwistedInt should be in range of (0 ~ "
            message += str((self.size - 1))
            message += ')'
            raise TypeError(message)
        else:
            return (self.list[first] * self.list[second])
