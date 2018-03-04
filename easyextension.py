from twistedint import *

"""
This file contains functions which implements the easy extensions.

"""

#Function for the first Easy extension.
def findMul1(n):
    """
    This function finds for a given n all elements x ∈ Zn such that x * x = 1, where 1 ∈ Zn is calculated as TwistedInt(1,n).
    :param n: is the n value of the twisted ints.

    >>> findMul1(0)
    []

    >>> findMul1(-1)
    []

    >>> findMul1(1)
    []

    >>> findMul1(5)
    [<1:2>]

    >>> findMul1(13)
    [<1:2>, <2:7>, <3:7>]
    """
    results = []
    for i in range (2, n): #We should skip the 1, because the TwistedInt(1,1) is an illegal expression!
        for j in range (0, i):
            ti = TwistedInt(j, i)
            if (ti * ti) == TwistedInt(1, i):
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

    >>> checkReverseAdd(0)
    True

    >>> checkReverseAdd(2)
    True

    Errors:
    >>> checkReverseAdd(-1)
    Trace (most recent call last):
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

    >>> checkReverseMultiply(350)
    True

    Errors:
    >>> checkReverseMultiply(-1)
    Trace (most recent call last):
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

    >>> checkReverseAddAndAdd(35)
    True

    Errors:
    >>> checkReverseAddAndAdd(-1)
    Trace (most recent call last):
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

    Errors:
    >>> checkReverseMultiplyAndMult(-1)
    Trace (most recent call last):
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

    Errors:
    >>> checkReverseNested(-1)
    Trace (most recent call last):
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
