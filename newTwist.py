class NewTwist:  # Class allows custom operations to be created and reused on this type of twistedint

    # when creating a newTwist runs
    def __init__(self, val, n):
        # These self. hold variables for the whole instance of the class
        self.addOperation = ""
        self.addExists = False
        self.multOperation = ""
        self.multExists = False
        self.openBrackets = 0
        self.remainingInput = ""
        if n < 0:  # checks that n is greater than 0
            raise ValueError("The range of the value should be greater than 0.")
        else:  # sets the variables for the newTwist
            self.val = val
            self.n = n

    # Overwrite "print" to print in correct format
    def __str__(self):
        return "<" + str(self.val) + ":" + str(self.n) + ">"

    def __repr__(self):
        return str(self)

    # Overwrite * to allow for use or creation of custom functions
    def __mul__(self, other):
        if not isinstance(self, other.__class__):  # checks that two of the same class are being multiplied
            raise TypeError("The type of the second argument is not the TwistedInt!")
        elif self.n != other.n:  # checks that both have the same value of n
            raise ValueError("The value n of the two objects should be same!")
        else:
            if not self.multExists:  # checks if a previous function for the instance exists
                # below allows for both main methods to create functions to be used for the *
                # it's a bit messy however it does work
                tempO = self.addOperation
                tempB = self.addExists

                self.addOperation = ""
                self.addExists = False

                self.createAdd(other)

                self.multOperation = True
                self.multOperation = self.addOperation
                self.addOperation = tempO
                self.addExists = tempB

            else:  # when a function already exists
                print("You already have a function to multiply something")
                print(self.multOperation)
                # asks if the user would like to use previously made function
                uInput = input("Would you like to use this function y = yes, n = create new function")
                while uInput != "y" and uInput != "n":  # ensure input is either y or n
                    uInput = input("Please enter either y or n")
                if uInput == "y":  # if they do want to use the previously made function
                    self.remainingInput = ""

                    tempO = self.addOperation
                    tempB = self.addExists

                    self.addOperation = self.multOperation
                    self.addExists = self.multExists

                    print(NewTwist(self.addLetter(other), self.n))

                    self.addOperation = tempO
                    self.addExists = tempB

                else:  # The user wants to create a new function
                    self.multOperation = ""
                    self.multOperation = False

                    tempO = self.addOperation
                    tempB = self.addExists

                    self.addOperation = ""
                    self.addExists = False

                    self.createAdd(other)

                    self.multOperation = self.addOperation
                    self.multExists = True

                    self.addOperation = tempO
                    self.addExists = tempB

    # Overwrite * to allow for use or creation of custom functions
    def __add__(self, other):
        if not isinstance(self, other.__class__):  # checks that two of the same class are being added
            raise TypeError("The type of the second argument is not the NewTwist!")
        elif self.n != other.n:  # checks that the two values of n are the same
            raise ValueError("The value n of the two objects should be same!")
        else:
            if not self.addExists:  # if a previous add function doesn't already exist
                self.createAdd(other)
            else:  # if a previous add function does exist
                print("You already have a function to add something")
                print(self.addOperation)
                # asks the user if they want to create a new one or not
                uInput = input("Would you like to use this function y = yes, n = create new function")
                while uInput != "y" and uInput != "n":  # ensure the user enters a valid input
                    uInput = input("Please enter either y or n")
                if uInput == "y":  # if they want to re-use the same function
                    self.remainingInput = ""
                    print(NewTwist(self.addLetter(other), self.n))
                else:  # create new function
                    self.addOperation = ""
                    self.addExists = False
                    self.createAdd(other)

    # Overwrite the == operator.
    def __eq__(self, other):
        if not isinstance(self, other.__class__):
            raise TypeError("The type of the second argument is not the NewTwist!")
        elif self.n != other.n:
            raise ValueError("The value n of the two objects should be same!")
        else:
            if self.n == other.n and self.val == other.val:
                return True
            return False

    # Overwrite the != operator.
    def __ne__(self, other):
        return not self.__eq__(other)

    # when the user wants to create a new function
    def createAdd(self, other):
        self.remainingInput = ""
        print(
            "When creating custom add function, the following notation will be used: NewTwist(a,n) + NewTwist(b,n)")
        print(NewTwist(self.addLetter(other), self.n))  # create, evaluates and prints function
        self.addExists = True  # says a function exists for later use

    # adds an operator to the function
    def addOperator(self, other, value):
        # if user is creating a new function
        if not self.addExists:
            print("Current operation is %s" % self.addOperation)  # prints what operation so far is
            uInput = input("Please enter one of the following operators +, -, *, /, ^, %, ). Enter q to evalualte")
            if uInput == "+":  # if the input is (in this case) "+"
                self.addOperation = self.addOperation + "+ "  # adds a "+" to the operation so far
                # performs operation of previously evaluated value and continues to ask user for input
                return value + self.addLetter(other)
            # the rest of these are the same as the "+" just for different operands
            elif uInput == "-":
                self.addOperation = self.addOperation + "- "
                return value - self.addLetter(other)
            elif uInput == "*":
                self.addOperation = self.addOperation + "* "
                return value * self.addLetter(other)
            elif uInput == "/":
                self.addOperation = self.addOperation + "/ "
                return value / self.addLetter(other)
            elif uInput == "^":
                self.addOperation = self.addOperation + "^ "
                return value ** self.addLetter(other)
            elif uInput == "%":
                self.addOperation = self.addOperation + "% "
                return value % self.addLetter(other)
            elif uInput == "q" and self.openBrackets == 0:  # if the user wants to stop adding things to the function
                                                            # also checks that there are no open brackets
                return value  # returns value as it is with no recursive calls
            elif uInput == ")" and self.openBrackets > 0:  # closes a bracket if one was open
                self.addOperation = self.addOperation + ") "
                self.openBrackets -= 1  # decrements the number of open brackets
                return value
            else:  # else must have been an invalid input so returns to top of function
                return self.addOperator(other, value)
        else:  # else uses predefined function
            if self.remainingInput == " " or self.remainingInput == "":  # if there is nothing left to parse
                return value
            else:  # else takes the input to be the first character in the remaining input to parse
                uInput = self.remainingInput[0]
                self.remainingInput = self.remainingInput[2:]  # remaining input is 2 characters from the start onwards
            if uInput == "+":  # works the same as above except this time doesn't print out current output
                return value + self.addLetter(other)
            elif uInput == "-":
                return value - self.addLetter(other)
            elif uInput == "*":
                return value * self.addLetter(other)
            elif uInput == "/":
                return value / self.addLetter(other)
            elif uInput == "^":
                return value ** self.addLetter(other)
            elif uInput == "%":
                return value % self.addLetter(other)
            elif uInput == ")" and self.openBrackets > 0:
                self.openBrackets -= 1
                return value
            else:  # as it must be a valid input to have been saved it shouldn't be possible to get here
                print(uInput)
                raise ValueError("Invalid Operation -- somehow")  # should not be possible to get here

    # adds the users inputted numbers to the function
    def addLetter(self, other):
        if not self.addExists:  # if the user is creating a new function
            print("Current operation is %s" % self.addOperation)
            uInput = input("Please enter either a, b, n, (")  # prints out list of valid inputs for the user
            if uInput == "a":  # works same as above except with letters (defined in createAdd function)
                self.addOperation = self.addOperation + "a "
                return self.addOperator(other, self.val)
            elif uInput == "b":
                self.addOperation = self.addOperation + "b "
                return self.addOperator(other, other.val)
            elif uInput == "n":
                self.addOperation = self.addOperation + "n "
                return self.addOperator(other, self.n)
            elif uInput == "(":  # if the user wants to use brackets
                self.addOperation = self.addOperation + "( "  # adds a bracket to the current function
                self.openBrackets += 1  # increments the number of open brackets
                # this works by calculating a value from nothing to be then passed in as a value for the other function
                return self.addOperator(other, self.addLetter(other))
            else:  # else was an invalid input
                return self.addLetter(other)
        else:
            if self.remainingInput == "":
                uInput = self.addOperation[0]
                self.remainingInput = self.addOperation[2:]
            else:  # else works exactly the same as above
                uInput = self.remainingInput[0]
                self.remainingInput = self.remainingInput[2:]
            if uInput == "a":
                return self.addOperator(other, self.val)
            elif uInput == "b":
                return self.addOperator(other, other.val)
            elif uInput == "n":
                return self.addOperator(other, self.n)
            elif uInput == "(":
                self.openBrackets += 1
                return self.addOperator(other, self.addLetter(other))
            else:
                print(uInput)
                raise ValueError("Invalid operation -- somehow")  # should never be able to get here
