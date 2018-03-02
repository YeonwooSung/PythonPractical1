from twistedintegers import *

class IteratorOfTwistedIntegers:
    def __init__(self, tis):
        if isinstance(tis, TwistedIntegers):
            self.tis = tis
            self.index = 0
        else:
            raise TypeError("This class takes the TwistedIntegers type instance as an argument!")

    def __iter__(self):
        return self #Because the class is the Iterator.

    def __next__(self):
        if self.index = self.tis.n:
            raise StopIteration
        else:
            ti = TwistedInt(self.index, self.tis.n)
            self.index += 1
            return ti
