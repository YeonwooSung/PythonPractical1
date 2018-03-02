from twistedint import *

class Matrix:

    def __init__(self):
        print("please enter the number of rows:")
        row = int(input())
        print("please enter the number of columns:")
        column = int(input())
        self.matrix = [[0 for x in range(column)] for y in range(row)]
        self.fillMatrix(self.matrix)


    def fillMatrix(self, matrix):

        #print("Have you already twistedInts made? y/n")
        #user = input()
        #while (user != "y" and user != "n"):
        #   print("please enter either y or n, or q to quit")
        #    user  = input()
        #    if (user == "q"):
        #        quit()

        #if (user == "n"):
        print("please enter the n value for all the twistedInts in the matrix")
        n = int(input())
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                print("Please enter the value for twistedInt at value %i, %i" % (i, j))
                uInput = int(input())
                while uInput >= n or uInput < 0:
                    print("please ensure that your value is less than %i" % n)
                    uInput = int(input())
                matrix[i][j] = TwistedInt(uInput, n)

        print(matrix)

        return matrix

    # Define the operator +
    def __add__(self, other):
        if not isinstance(self, other.__class__):
            raise TypeError("The type of the second argument is not a matrix")
        elif len(self) != len(other) or len(self[0]) != len(other[0]):
            raise TypeError("The matrices can't be added as they are different sizes")
        else:
            output = [[0 for x in range(len(self[0]))] for y in range(len(self))]
            for i in range(len(self)):
                for j in range(len(self[i])):
                    output[i][j] = self[i][j] + other[i][j]
            return output

    def __len__(self):
        return len(self.matrix)

    def __getitem__(self, item):
        return self.matrix[item]

    def __mul__(self, other):
        if not isinstance(self, other.__class__):
            if TwistedInt == type(other):
                output = [[0 for x in range(len(self[0]))] for y in range(len(self))]
                for i in range(len(output)):
                    for j in range(len(output[i])):
                        output[i][j] = self[i][j] * other
                return output
            else:
                print(type(other))
                raise TypeError("Please multiply a matrix by another matrix or a twisted int")
        elif len(self) != len(other[0]) and len(self[0]) != len(other):
            raise TypeError("The matrices can't be multiplied as they are different sizes")
        else:
            output = [[0 for x in range(len(other[0]))] for y in range(len(self))]
            for i in range(len(output)):
                for j in range(len(output[i])):
                    part = TwistedInt(0, self.matrix[0][0].n)
                    for columns in range(len(self.matrix[0])):
                        part = part + self.matrix[i][columns] * other[columns][j]
                    output[i][j] = part
            return output





