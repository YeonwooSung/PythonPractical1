from twistedint import *

class TwistedIntegers:
    def __init__(self, n):
        self.size = n #Add a field called size, which is the size of Zn, which is a set of TwistedInts.
        self.list = [] #The list which cotains all twisted int objects in it
        for i in range(0, n):
            self.list.append(TwistedInt(i, n))

    #This method will be used for printing out the TwistedInteger.
    def __str__(self):
        return str(self.list) #Return the string of the list

    #To represent the instance of TwitedInteger
    def __repr__(self):
        return str(self.list) #Return the string of the list

    #This will return the size of the Zn, which is a set of TwistedInts.
    def Size(self):
        return self.size

    #This will return the list of TwistedInt object.
    def IntegerList(self):
        return self.list

    #This method adds 2 TwistedInt objects
    def addTwoTwistedInt(self, first, second):
        if (not (0 < first < self.size)) or (not (0 < second < self.size)):#To check if the arguments are in the range
            message = "The value of the TwistedInt should be in range of (0 ~ "
            message += str((self.size - 1))
            message += ')'
            raise TypeError(message)
        else:
            return (self.list[first] + self.list[second])

    #This method multiplies 2 TwistedInt objects
    def mulTwoTwistedInt(self, first, second):
        if (not (0 < first < self.size)) or (not (0 < second < self.size)):#To check if the arguments are in the range
            message = "The value of the TwistedInt should be in range of (0 ~ "
            message += str((self.size - 1))
            message += ')'
            raise TypeError(message)
        else:
            return (self.list[first] * self.list[second])
