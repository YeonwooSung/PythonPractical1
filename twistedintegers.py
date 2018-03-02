from twistedint import *

class TwistedIntegers:
    def __init__(self, n):
        if n <= 0:
            raise ValueError("n must be a positive integer")
        else:
            self.size = n

    def __str__(self):
        string = "{"
        for i in range(self.size):
            string += str(TwistedInt(i, self.size))
            if i < self.size - 1:
                string += ", "
        string += "}"
        return string

    def __repr__(self):
        return str(self)

    def Size(self):
        return self.size
