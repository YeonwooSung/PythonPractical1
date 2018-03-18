from twistedint import *


# creates and peforms operations on matrices
class Matrix:
    # asks user to specify size and fill matrix on creation
    def __init__(self, premade=None):
        if premade is not None:
            self.matrix = premade
        else:
            print("please enter the number of rows:")
            row = int(input())
            print("please enter the number of columns:")
            column = int(input())
            self.matrix = [[0 for x in range(column)] for y in range(row)]  # creates an empty matrix to be filled
            self.fillMatrix(self.matrix)  # calls method to fill matrix

    # gets user to fill a matrix with number
    def fillMatrix(self, matrix):
        print("please enter the n value for all the twistedInts in the matrix")
        n = int(input())  # gets value for n
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):  # for each cell in the matrix
                print("Please enter the value for twistedInt at value %i, %i" % (i, j))
                uInput = int(input())
                while uInput >= n or uInput < 0:  # if input is invalid for a twisted int reject it
                    print("please ensure that your value is less than %i" % n)
                    uInput = int(input())
                matrix[i][j] = TwistedInt(uInput, n)  # sets cell to TwistedInt
        return matrix

    # Define the operator +
    def __add__(self, other):
        if not isinstance(self, other.__class__):  # if trying to add something else to a matrix
            raise TypeError("The type of the second argument is not a matrix")
        elif len(self) != len(other) or len(self[0]) != len(other[0]):  # if the matrices aren't the same size
            raise TypeError("The matrices can't be added as they are different sizes")
        else:
            output = [[0 for x in range(len(self[0]))] for y in range(len(self))]  # create an empty output matrix
            for i in range(len(self)):  # for each cell in the matrix
                for j in range(len(self[i])):
                    output[i][j] = self[i][j] + other[i][j]  # use TwistedInt addition to add
            return Matrix(output)

    # Defines the len() for the matrix
    def __len__(self):
        return len(self.matrix)

    # defines getting an item at an index
    def __getitem__(self, item):
        return self.matrix[item]

    # Defines the * operator
    def __mul__(self, other):
        if not isinstance(self, other.__class__):  # if multiplying a matrix by something else
            if TwistedInt == type(other):  # if the other thing is a twisted int
                output = [[0 for x in range(len(self[0]))] for y in range(len(self))]
                for i in range(len(output)):
                    for j in range(len(output[i])):
                        output[i][j] = self[i][j] * other  # multiplies all cells in the matrix by twisted int
                return Matrix(output)
            else:  # else invalid type
                raise TypeError("Please multiply a matrix by another matrix or a twisted int")
        elif len(self) != len(other[0]) and len(self[0]) != len(other):  # if the sizes don't work for multiplication
            raise TypeError("The matrices can't be multiplied as they are different sizes")
        else:  # else multiply the matrices
            output = [[0 for x in range(len(other[0]))] for y in range(len(self))]  # creates empty output
            for i in range(len(output)):
                for j in range(len(output[i])):  # for each cell in the output
                    part = TwistedInt(0, self.matrix[0][0].n)  # empty twisted int to be used to add things too
                    for columns in range(len(self.matrix[0])):  # calculates the correct output for the cell
                        part = part + self.matrix[i][columns] * other[columns][j]  # uses twistedInt multiplication
                    output[i][j] = part  # sets the cell to be the calculated twisted int
            return Matrix(output)

    # Overwrite "print"
    def __str__(self):

        output = "["
        for i in range(len(self.matrix) - 1):
            output = output + str(self.matrix[i]) + ",\n "
        output = output + str(self.matrix[len(self.matrix) - 1])
        output = output + "]"

        return output

    def __repr__(self):
        return str(self)
