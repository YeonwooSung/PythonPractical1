from Matrices import *

class TwistedInt:
    def __init__(self, val, n):
        if n < 0:
            raise ValueError("The range of the value should be greater than 0.")
        elif (n <= val) or (0 > val):
            raise ValueError("The value should be in the range of 0 ~ n")
        else :
            self.val = val
            self.n = n

    # Overwrite "print"
    def __str__(self):
        return "<" + str(self.val) + ":" + str(self.n) + ">"

    # Define the operator +
    def __add__(self, other):
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
        if isinstance(self, other.__class__):
            return self.val == other.val and self.n == other.n
        return False

    # Overwrite the function ne to define the operator !=
    def __ne__(self, other):
        return not self.__eq__(other)

    # Overwrite the repr function to represent the object with the format that we want.
    def __repr__(self):
        return str(self)
