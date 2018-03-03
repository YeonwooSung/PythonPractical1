class NewTwist:

    def __init__(self, val, n):
        self.addOperation = ""
        self.operationExists = False
        if n < 0:
            raise ValueError("The range of the value should be greater than 0.")
        elif (n <= val) or (0 > val):
            raise ValueError("The value should be in the range of 0 ~ n")
        else:
            self.val = val
            self.n = n

    # Overwrite "print"
    def __str__(self):
        return "<" + str(self.val) + ":" + str(self.n) + ">"

    def __add__(self, other):
        if not isinstance(self, other.__class__):
            raise TypeError("The type of the second argument is not the TwistedInt!")
        elif self.n != other.n:
            raise ValueError("The value n of the two objects should be same!")
        else:
            if not self.operationExists:
                self.createAdd(other)
            else:
                print("You already have a function to add something")
                print(self.addOperation)
                uInput = input("Would you like to use this function y = yes, n = create new function")
                while uInput != "y" and uInput != "n":
                    uInput = input("Please enter either y or n")
                if uInput == "y":
                    remainingInput = ""
                    print(self.addLetter(other, remainingInput))
                else:
                    self.addOperation = ""
                    self.operationExists = False
                    self.createAdd(other)

    def addOperator(self, other, value, remainingInput):
        if not self.operationExists:
            print("Current operation is %s" % self.addOperation)
            uInput = input("Please enter one of the following operators +, -, *, /, ^, % . Enter q to quit")
            if uInput == "+":
                self.addOperation = self.addOperation + "+ "
                return value + self.addLetter(other, remainingInput)
            elif uInput == "-":
                self.addOperation = self.addOperation + "- "
                return value - self.addLetter(other, remainingInput)
            elif uInput == "*":
                self.addOperation = self.addOperation + "* "
                return value * self.addLetter(other, remainingInput)
            elif uInput == "/":
                self.addOperation = self.addOperation + "/ "
                return value / self.addLetter(other, remainingInput)
            elif uInput == "^":
                self.addOperation = self.addOperation + "^ "
                return value ** self.addLetter(other, remainingInput)
            elif uInput == "%":
                self.addOperation = self.addOperation + "% "
                return value % self.addLetter(other, remainingInput)
            elif uInput == "q":
                self.operationExists = True
                return value
            else:
                return self.addOperator(other, value, remainingInput)
        else:
            if remainingInput == " " or remainingInput == "":
                return value
            else:
                uInput = remainingInput[0]
                remainingInput = remainingInput[2:]
            if uInput == "+":
                return value + self.addLetter(other, remainingInput)
            elif uInput == "-":
                return value - self.addLetter(other, remainingInput)
            elif uInput == "*":
                return value * self.addLetter(other, remainingInput)
            elif uInput == "/":
                return value / self.addLetter(other, remainingInput)
            elif uInput == "^":
                return value ** self.addLetter(other, remainingInput)
            elif uInput == "%":
                return value % self.addLetter(other, remainingInput)
            else:
                raise ValueError("Invalid Operation -- somehow")  # should not be possible to get here

    def addLetter(self, other, remainingInput):
        if not self.operationExists:
            print("Current operation is %s" % self.addOperation)
            uInput = input("Please enter either a or b or n")
            if uInput == "a":
                self.addOperation = self.addOperation + "a "
                return self.addOperator(other, self.val, remainingInput)
            elif uInput == "b":
                self.addOperation = self.addOperation + "b "
                return self.addOperator(other, other.val, remainingInput)
            elif uInput == "n":
                self.addOperation = self.addOperation + "n "
                return self.addOperator(other, self.n, remainingInput)
            else:
                return self.addLetter(other, remainingInput)
        else:
            if remainingInput == "":
                uInput = self.addOperation[0]
                remainingInput = self.addOperation[2:]
            else:
                uInput = remainingInput[0]
                remainingInput = remainingInput[2:]
            if uInput == "a":
                return self.addOperator(other, self.val, remainingInput)
            elif uInput == "b":
                return self.addOperator(other, other.val, remainingInput)
            elif uInput == "n":
                return self.addOperator(other, self.n, remainingInput)
            else:
                raise ValueError("Invalid operation -- somehow")  # should never be able to get here

    def createAdd(self, other):
        remainingInput = ""
        print("When creating custom add function, the following notation will be used: NewTwist(a,n) + NewTwist(b,n)")
        input("Please press y to continue")
        print(self.addLetter(other, remainingInput))
