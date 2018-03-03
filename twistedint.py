from Matrices import *

"""
This is the module called twistedint, which is to extend the implementation of the "twisted integers".

"""
class TwistedInt:
    def __init__(self, val, n):
        """
        Creates a new instance of the TwistedInt object.
        If the n is less than 0, or the value is greater than or equal to n, the  error occurs.
        :param value: is the value of the twisted int.
        :param n: is the n value of the twisted int, which is the modulo.

        >>> TwistedInt(2, 5)
        <2:5>

        Errors:
        >>> TwistedInt(1, 1)
        Traceback (most recent call last):
        ...
        ValueError: The value should be in the range of 0 ~ n-1

        >>> TwistedInt(-2, -5)
        Traceback (most recent call last):
        ...
        ValueError: The range of the value should be greater than 0.
        """
        if n < 0:
            raise ValueError("The range of the value should be greater than 0.")
        elif (n <= val) or (0 > val):
            raise ValueError("The value should be in the range of 0 ~ n-1")
        else :
            self.val = val
            self.n = n

    # Overwrite "print"
    def __str__(self):
        """
        This method converts the instance of the TwistedInt class to the corresponding string.
        :return: (string) the string representation

        >>> str(TwistedInt(3, 7))
        '<5:7>'
        """
        return "<" + str(self.val) + ":" + str(self.n) + ">"

    # Define the operator +
    def __add__(self, other):
        """
        Defines the operation of addition.
        :param other: this is the another twisted int object, which is the second operand of the addition.

        >>> TwistedInt(2, 5) + TwistedInt(3, 5)
        <0,5>

        Errors:
        >>> TwistedInt(2,7) + TwistedInt(1, 8)
        Traceback (most recent call last):
        ...
        ValueError: The value n of the two objects should be same!

        >>> TwistedInt(2, 5) + 35
        Traceback (most recent call last):
        ...
        TypeError: The type of the second argument is not the TwistedInt!
        """
        if not isinstance(self, other.__class__):
            raise TypeError("The type of the second argument is not the TwistedInt!")
        elif self.n != other.n:
            raise ValueError("The value n of the two objects should be same!")
        else:
            return TwistedInt((self.val + other.val) % self.n, self.n)

    # Define the operator *
    def __mul__(self, other):
        if not isinstance(self, other.__class__):
            if other.__class__ == "<class 'Matrices.Matrix'>":
                return other * self
            else:
                raise TypeError("The type of the second argument is not the TwistedInt!")
        elif self.n != other.n:
            raise ValueError("The value n of the two objects should be same!")
        else:
            return TwistedInt((self.val + other.val + self.val * other.val) % self.n, self.n)

    # Overwrite the function eq to define the operator ==
    def __eq__(self, other):
        """
        Defines the operation of equality (operator ==).
        :param other: is the object the current one is compared to.
        :return: True | False

        >>> TwistedInt(3, 5) == TwistedInt(3, 5)
        True

        >>> TwistedInt(2, 5) == TwistedInt(3, 5)
        False

        >>> TwistedInt(2, 3) == 4
        False
        """
        if isinstance(self, other.__class__):
            return self.val == other.val and self.n == other.n
        return False

    # Overwrite the function ne to define the operator !=
    def __ne__(self, other):
        """
        Defines the operation of inequality (opeartor !=).
        :param other: is the object that will be compared with the self thing.
        :return: True | False

        >>> TwistedInt(2, 3) != TwistedInt(3, 4)
        True

        >>> TwistedInt(2, 3) != TwistedInt(2, 3)
        False

        >>> TwistedInt(2, 3) != 3
        True
        """
        return not self.__eq__(other)

    # Overwrite the repr function to represent the object with the format that we want.
    def __repr__(self):
        """
        Similar with __str__ method.
        :return: (string) the string representation

        >>> repr(TwistedInt(3, 7))
        '<5:7>'
        """
        return str(self)
