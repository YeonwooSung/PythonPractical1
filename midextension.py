from twistedintegers import *

"""
This file contains all functions and methods for the medium extensions.

"""

class IteratorOfTwistedIntegers:
    def __init__(self, tis):
        """
        Creates a new IteratorOfTwistedIntegers type object.
        :param tis: is the target TwistedIntegers object that the user wants to iterate.

        Errors:
        >>> IteratorOfTwistedIntegers(5)
        Traceback (most recent call last):
        ...
        TypeError: This class takes the TwistedIntegers type instance as an argument!
        """
        if isinstance(tis, TwistedIntegers):
            self.tis = tis
            self.index = 0
        else:
            raise TypeError("This class takes the TwistedIntegers type instance as an argument!")

    def __iter__(self):
        """
        This method defines the class as an iterator.

        :return: self
        """
        return self #Because the class is the Iterator.

    def __next__(self):
        """
        This method defines how the twisted integers will be iterated through.
        It will stop the iteration when the index of the iteration is at the end of the set.

        :return: next TwistedInt in the given TwistedIntegers.
        """
        if self.index == self.tis.size:
            raise StopIteration
        else:
            ti = TwistedInt(self.index, self.tis.size)
            self.index += 1
            return ti

def modArithmetic(n, f):
    """
    This function tests if the return value of the f(op1, op2) is equals to the op2 for all op2 in the given TwistedIntegers object.

    :param n: is the given n value to define the TwistedIntegers object.
    :param f: is the function to apply test to all TwistedInts in the TwistedIntegers.
    :return: results is the list of every op1 that passes the given test.
    """
    results = []
    for op1 in IteratorOfTwistedIntegers(TwistedIntegers(n)):
        for op2 in IteratorOfTwistedIntegers(TwistedIntegers(n)):
            if f(op1, op2) != op2: #if not true for op2, then terminate the loop
                break
            if op2.val == (n - 1): #if this condition has been true for op2, then append op1 to the list of results.
                results.append(op1)
    return results

def addModArithmetic(n):
    """
    This function checks if the addition follows modular modular arithmetic rule, which is "op1 + op2 == op1".

    >>> addModArithmetic(4)
    [<0:4>]

    Errors:
    >>> addModArithmetic(-1)
    Traceback (most recent call last):
    ...
    ValueError: The range of the value should be greater than 0.
    """
    if (n < 0):
        raise ValueError("The range of the value should be greater than 0.")
    return modArithmetic(n, lambda m, i: m + i)

def multModArithmetic(n):
    """
    This function checks if the multiplication follows modular arithmetic rule, which is "op1 * op2 == op1".

    >>> multModArithmetic(4)
    [<0:4>]

    Errors:
    >>> multModArithmetic(-1)
    Traceback (most recent call last):
    ...
    ValueError: The range of the value should be greater than 0.
    """
    if (n < 0):
        raise ValueError("The range of the value should be greater than 0.")
    return modArithmetic(n, lambda m, i: m * i)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
