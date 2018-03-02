from twistedint import *

# Function for the first Easy extension.
def findMull(n):
    results = []
    for i in range (2, n):  # We should skip the 1, because the TwistedInt(1,1) is an illegal expression!
        for j in range (0, i):
            ti = TwistedInt(j, i)
            if (ti * ti) == TwistedInt(1, i):
                results.append(ti)
    return results

#Function for the second Easy extension.
def checkReverse(n, commandNum):
    if commandNum == 1:
        return checkReverseAdd(n)
    elif commandNum == 2:
        return checkReverseMultiply(n)
    elif commandNum == 3:
        return checkReverseAddAndMult(n)
    elif commandNum == 4:
        return checkReverseMultiplyAndMult(n)
    elif commandNum == 5:
        return checkReverseNested(n)
    else:
        raise ValueError("Wrong command number! The second parameter should be the value between 1 to 5")

#Function to check if the condition "x+y == y+x" is true
def checkReverseAdd(n):
    for x in range (0, n-1):
        for y in range (0, n-1):
            ti1 = TwistedInt(x, n)
            ti2 = TwistedInt(y, n)
            if not ((ti1 + ti2) == (ti2 + ti1)):
                return False
    return True

#Function to check if the condition "x*y == y*x" is true
def checkReverseMultiply(n):
    for x in range (0, n-1):
        for y in range (0, n-1):
            ti1 = TwistedInt(x, n)
            ti2 = TwistedInt(y, n)
            if not ((ti1 * ti2) == (ti2 * ti1)):
                return False
    return True

#Function to check if the condition "(x+y)* z == x+(y*z)" is true
def checkReverseAddAndAdd(n):
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
    for x in range (0, n-1):
        for y in range (0, n-1):
            for z in range (0, n-1):
                ti1 = TwistedInt(x, n)
                ti2 = TwistedInt(y, n)
                ti3 = TwistedInt(z, n)
                if not (((ti1*ti2)*ti3) == (ti1*(ti2*ti3))):
                    return False
    return True

#Function to check if the condition "(x+y)*z == (x*z)+(y*z)"
def checkReverseNested(n):
    for x in range (0, n-1):
        for y in range (0, n-1):
            for z in range (0, n-1):
                ti1 = TwistedInt(x, n)
                ti2 = TwistedInt(y, n)
                ti3 = TwistedInt(z, n)
                if not (((ti1+ti2)*ti3) == ((ti1*ti3) + (ti2*ti3))):
                    return False
    return True
