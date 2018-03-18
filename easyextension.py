from twistedint import *

"""
This file contains functions which implements the easy extensions.

"""

#Function for the first Easy extension.
def findMul1(n):
    """
    This function finds for a given n all elements x in the Zn.
    :param n: is the n value of the twisted ints.

    >>> findMul1(0)
    []

    >>> findMul1(-1)
    []

    >>> findMul1(7)
    [<2:7>, <3:7>]

    >>> findMul1(14)
    [<3:14>, <9:14>]

    >>> findMul1(23)
    [<4:23>, <17:23>]

    >>> findMul1(46)
    [<17:46>, <27:46>]

    >>> findMul1(54)
    []

    Errors:
    >>> findMul1(1)
    Traceback (most recent call last):
    ...
    ValueError: The value of the TwistedInt should be in the range of 0 ~ n-1
    """
    results = []
    for i in range (0, n): #We should skip the 1, because the TwistedInt(1,1) is an illegal expression!
        ti = TwistedInt(i, n)
        if (ti * ti) == TwistedInt(1, n):
            results.append(ti)
    return results

#Function for the second Easy extension.
def checkReverse(n, commandNum):
    """
    This function gets the input, and does the corresponding task.
    If the commandNum is 1, it will call the function checkReverseAdd.
    If the commandNum is 2, it will call the function checkReverseMultiply.
    If the commandNum is 3, it will call the function checkReverseAddAndAdd.
    If the commandNum is 4, it will call the function checkReverseMultiplyAndMult.
    If the commandNum is 5, it will call the function checkReverseNested.
    :param n: is the n value of the TwistedInt.
    :param commandNum: is the number which determines the task to do.

    >>> checkReverse(3, 1)
    True

    >>> checkReverse(3, 2)
    True

    >>> checkReverse(3, 3)
    True

    >>> checkReverse(3, 4)
    True

    >>> checkReverse(3, 5)
    False
    """
    if commandNum == 1:
        return checkReverseAdd(n)
    elif commandNum == 2:
        return checkReverseMultiply(n)
    elif commandNum == 3:
        return checkReverseAddAndAdd(n)
    elif commandNum == 4:
        return checkReverseMultiplyAndMult(n)
    elif commandNum == 5:
        return checkReverseNested(n)
    else:
        raise ValueError("Wrong command number! The second parameter should be the value between 1 to 5")

#Function to check if the condition "x+y == y+x" is true
def checkReverseAdd(n):
    """
    This function checks if the condition "x+y == y+x" is true for all twisted ints in the given range.

    >>> checkReverseAdd(1)
    True

    >>> checkReverseAdd(2)
    True

    >>> checkReverseAdd(13)
    True

    >>> checkReverseAdd(23)
    True

    >>> checkReverseAdd(50)
    True

    >>> checkReverseAdd(100)
    True

    Errors:
    >>> checkReverseAdd(-1)
    Traceback (most recent call last):
    ...
    ValueError: The range of the value should be greater than 0.
    """
    if (n < 0):
        raise ValueError("The range of the value should be greater than 0.")
    for x in range (0, n-1):
        for y in range (0, n-1):
            ti1 = TwistedInt(x, n)
            ti2 = TwistedInt(y, n)
            if not ((ti1 + ti2) == (ti2 + ti1)):
                return False
    return True

#Function to check if the condition "x*y == y*x" is true
def checkReverseMultiply(n):
    """
    This function checks if the condition "x*y == y*x" is true for all twisted ints in the given range.

    >>> checkReverseMultiply(3)
    True

    >>> checkReverseMultiply(6)
    True

    >>> checkReverseMultiply(13)
    True

    >>> checkReverseMultiply(35)
    True

    >>> checkReverseMultiply(350)
    True

    Errors:
    >>> checkReverseMultiply(-1)
    Traceback (most recent call last):
    ...
    ValueError: The range of the value should be greater than 0.
    """
    if (n < 0):
        raise ValueError("The range of the value should be greater than 0.")
    for x in range (0, n-1):
        for y in range (0, n-1):
            ti1 = TwistedInt(x, n)
            ti2 = TwistedInt(y, n)
            if not ((ti1 * ti2) == (ti2 * ti1)):
                return False
    return True

#Function to check if the condition "(x+y)+ z == x+(y+z)" is true
def checkReverseAddAndAdd(n):
    """
    This function checks if the condition "(x+y)+ z == x+(y+z)" is true for all twisted ints in the given range.

    >>> checkReverseAddAndAdd(0)
    True

    >>> checkReverseAddAndAdd(1)
    True

    >>> checkReverseAddAndAdd(35)
    True

    >>> checkReverseAddAndAdd(60)
    True

    >>> checkReverseAddAndAdd(85)
    True

    Errors:
    >>> checkReverseAddAndAdd(-1)
    Traceback (most recent call last):
    ...
    ValueError: The range of the value should be greater than 0.
    """
    if (n < 0):
        raise ValueError("The range of the value should be greater than 0.")
    for x in range (0, n-1):
        for y in range (0, n-1):
            for z in range (0, n-1):
                ti1 = TwistedInt(x, n)
                ti2 = TwistedInt(y, n)
                ti3 = TwistedInt(z, n)
                if not (((ti1 + ti2)+ti3) == (ti1+(ti2+ti3))):
                    return False
    return True

#Function to check if the condition "(x*y)*z == x*(y*z)" is true
def checkReverseMultiplyAndMult(n):
    """
    This function checks if the condition "(x*y)*z == x*(y*z)" is true for all twisted ints in the given range.

    >> checkReverseMultiplyAndMult(3)
    True

    >>> checkReverseMultiplyAndMult(23)
    True

    >>> checkReverseMultiplyAndMult(45)
    True

    >>> checkReverseMultiplyAndMult(80)
    True

    >>> checkReverseMultiplyAndMult(100)
    True

    Errors:
    >>> checkReverseMultiplyAndMult(-1)
    Traceback (most recent call last):
    ...
    ValueError: The range of the value should be greater than 0.
    """
    if (n < 0):
        raise ValueError("The range of the value should be greater than 0.")
    for x in range (0, n-1):
        for y in range (0, n-1):
            for z in range (0, n-1):
                ti1 = TwistedInt(x, n)
                ti2 = TwistedInt(y, n)
                ti3 = TwistedInt(z, n)
                if not (((ti1*ti2)*ti3) == (ti1*(ti2*ti3))):
                    return False
    return True

#Function to check if the condition "(x+y)*z == (x*z)+(y*z)" is true
def checkReverseNested(n):
    """
    This function checks if the condition "(x+y)*z == (x*z)+(y*z)" is true for all twisted ints in the given range.

    >>> checkReverseNested(2)
    True

    >>> checkReverseNested(5)
    False

    >>> checkReverseNested(34)
    False

    >>> checkReverseNested(50)
    False

    >>> checkReverseNested(64)
    False

    >>> checkReverseNested(81)
    False

    >>> checkReverseNested(100)
    False

    Errors:
    >>> checkReverseNested(-1)
    Traceback (most recent call last):
    ...
    ValueError: The range of the value should be greater than 0.
    """
    if (n < 0):
        raise ValueError("The range of the value should be greater than 0.")
    for x in range (0, n-1):
        for y in range (0, n-1):
            for z in range (0, n-1):
                ti1 = TwistedInt(x, n)
                ti2 = TwistedInt(y, n)
                ti3 = TwistedInt(z, n)
                if not (((ti1+ti2)*ti3) == ((ti1*ti3) + (ti2*ti3))):
                    return False
    return True

if __name__ == "__main__":
    import doctest
    doctest.testmod()
