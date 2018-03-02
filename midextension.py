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

def modArithmetic(n, f):
    results = []
    for op1 in IteratorOfTwistedIntegers(TwistedIntegers(n)):
        for op2 in IteratorOfTwistedIntegers(TwistedIntegers(n)):
            if f(op1, op2) != op2: #if not true for op2, then terminate the loop
                break
            if op2.val == (n - 1): #if this condition has been true for op2, then append op1 to the list of results.
                results.append(op1)
    return results

def addModArithmetic(n):
    return modArithmetic(n, lambda m, i: m + i)

def multModArithmetic(n):
    return modArithmetic(n, lambda m, i: m * i)
