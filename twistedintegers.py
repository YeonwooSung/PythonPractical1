from twistedint import *
"""
This is the module called twistedintegers.

"""
class TwistedIntegers:
    def __init__(self, n):
        """
        Creates a new TwitedIntegers object.

        :param n: is the size of the twisted integers.

        >>> TwistedIntegers(5)
        [<0:5>, <1:5>, <2:5>, <3:5>, <4:5>]

        >>> TwistedIntegers(10)
        [<0:10>, <1:10>, <2:10>, <3:10>, <4:10>, <5:10>, <6:10>, <7:10>, <8:10>, <9:10>]

        >>> TwistedIntegers(0)
        []

        >>> TwistedIntegers(-1)
        []

        >>> TwistedIntegers(-10)
        []
        """
        self.size = n #Add a field called size, which is the size of Zn, which is a set of TwistedInts.
        self.list = [] #The list which cotains all twisted int objects in it
        for i in range(0, n):
            self.list.append(TwistedInt(i, n))

    #This method will be used for printing out the TwistedInteger.
    def __str__(self):
        """
        This returns the string of the list that contains n twisted ints in the twisted integers.

        :return: (self.list) contains n twisted int objects.

        >>> str(TwistedIntegers(1))
        '[<0:1>]'

        >>> str(TwistedIntegers(0))
        '[]'

        >>> str(TwistedIntegers(-1))
        '[]'

        >>> str(TwistedIntegers(-10))
        '[]'

        >>> str(TwistedIntegers(5))
        '[<0:5>, <1:5>, <2:5>, <3:5>, <4:5>]'
        """
        return str(self.list) #Return the string of the list

    #To represent the instance of TwitedInteger
    def __repr__(self):
        """
        Similar with the str method.

        :return: (self.list) contains n twisted int objects.

        >>> repr(TwistedIntegers(1))
        '[<0:1>]'

        >>> repr(TwistedIntegers(0))
        '[]'

        >>> repr(TwistedIntegers(-1))
        '[]'

        >>> repr(TwistedIntegers(-10))
        '[]'

        >>> repr(TwistedIntegers(5))
        '[<0:5>, <1:5>, <2:5>, <3:5>, <4:5>]'
        """
        return str(self.list) #Return the string of the list

    #This will return the size of the Zn, which is a set of TwistedInts.
    def Size(self):
        """
        This method returns the size of the twisted integers.

        :return: (self.size) is the size of the twisted integers.

        >>> TwistedIntegers(5).Size()
        5
        """
        return self.size

    #This will return the list of TwistedInt object.
    def IntegerList(self):
        """
        This method returns the list of the TwistedInts.

        :return: (self.list) is the list of the TwistedInts.

        >>> TwistedIntegers(5).IntegerList()
        [<0:5>, <1:5>, <2:5>, <3:5>, <4:5>]

        >>> TwistedIntegers(0).IntegerList()
        []

        >>> TwistedIntegers(-1).IntegerList()
        []

        >>> TwistedIntegers(-10).IntegerList()
        []

        >>> TwistedIntegers(10).IntegerList()
        [<0:10>, <1:10>, <2:10>, <3:10>, <4:10>, <5:10>, <6:10>, <7:10>, <8:10>, <9:10>]
        """
        return self.list

    #This method adds 2 TwistedInt objects
    def addTwoTwistedInt(self, first, second):
        """
        This method adds 2 TwistedInt objects in the current TwistedIntegers object.

        :param first: is the index of the first operand.
        :param second: is the index of the second operand.

        >>> TwistedIntegers(5).addTwoTwistedInt(3, 4)
        <2:5>

        >>> TwistedIntegers(10).addTwoTwistedInt(5, 6)
        <1:10>

        >>> TwistedIntegers(30).addTwoTwistedInt(5, 6)
        <11:30>

        >>> TwistedIntegers(50).addTwoTwistedInt(5, 6)
        <11:50>

        >>> TwistedIntegers(70).addTwoTwistedInt(5, 6)
        <11:70>

        >>> TwistedIntegers(90).addTwoTwistedInt(5, 6)
        <11:90>

        >>> TwistedIntegers(50).addTwoTwistedInt(5, 66)
        <71:50>

        Errors:
        >>> TwistedIntegers(5).addTwoTwistedInt(5, 4)
        Traceback (most recent call last):
        ...
        TypeError: The value of the TwistedInt should be in the range of 0 ~ 4

        >>> TwistedIntegers(2).addTwoTwistedInt(1, 2)
        Traceback (most recent call last):
        ...
        TypeError: The value of the TwistedInt should be in the range of 0 ~ 1
        """
        if (not (0 < first < self.size)) or (not (0 < second < self.size)):#To check if the arguments are in the range
            message = "The value of the TwistedInt should be in the range of 0 ~ "
            message += str((self.size - 1))
            raise TypeError(message)
        else:
            return (self.list[first] + self.list[second])

    #This method multiplies 2 TwistedInt objects
    def mulTwoTwistedInt(self, first, second):
        """
        This method adds 2 TwistedInt objects in the current TwistedIntegers object.

        :param first: is the index of the first operand.
        :param second: is the index of the second operand.

        >>> TwistedIntegers(5).mulTwoTwistedInt(3, 4)
        <4:5>

        >> TwistedIntgers(10).mulTwoTwistedInt(7, 9)
        <9:10>

        >>> TwistedIntegers(30).mulTwoTwistedInt(20, 25)
        <5:30>

        Errors:
        >>> TwistedIntegers(5).addTwoTwistedInt(5, 4)
        Traceback (most recent call last):
        ...
        TypeError: The value of the TwistedInt should be in the range of 0 ~ 4

        >>> TwistedIntegers(2).mulTwoTwistedInt(1, 2)
        Traceback (most recent call last):
        ...
        TypeError: The value of the TwistedInt should be in the range of 0 ~ 1
        """
        if (not (0 < first < self.size)) or (not (0 < second < self.size)):#To check if the arguments are in the range
            message = "The value of the TwistedInt should be in the range of 0 ~ "
            message += str((self.size - 1))
            raise TypeError(message)
        else:
            return (self.list[first] * self.list[second])

if __name__ == "__main__":
    import doctest
    doctest.testmod()
