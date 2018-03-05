import unittest
from unittest import mock
import sys
import io
from Matrices import *


class TestMatrices(unittest.TestCase):
    # Tests the creation of matrices works
    # The nature of the tests also test that the __getitem__ method works too
    def testInit(self):
        # This line mocks the users input for each time user input is required
        with mock.patch('builtins.input', side_effect=[2, 3, 5, 1, 4, 2, 3, 1, 3]):
            a = Matrix()
            matrixlist = [1, 4, 2, 3, 1, 3]  # a list of all the values in the matrix
            counter = 0  # to keep place in the matrixlist
            for i in range(2):  # tests for every value in the matrix
                for j in range(3):
                    self.assertEqual(a[i][j], TwistedInt(matrixlist[counter], 5), "Matrix should be filled correctly")
                    counter += 1
        # This line mocks the users input for each time user input is required
        with mock.patch('builtins.input', side_effect=[5, 2, 10, 6, 1, 9, 1, 5, 6, 2, 4, 6, 7]):
            a = Matrix()
            matrixlist = [6, 1, 9, 1, 5, 6, 2, 4, 6, 7]  # a list of all the values in the matrix
            counter = 0
            for i in range(5):  # tests every value in the matrix
                for j in range(2):
                    self.assertEqual(a[i][j], TwistedInt(matrixlist[counter], 10))
                    counter += 1

    # Tests that the len() for the matrix is working correctly
    def testLen(self):
        # This line mocks the users input for each time user input is required
        with mock.patch('builtins.input', side_effect=[3, 2, 5, 1, 3, 2, 4, 2, 3]):
            a = Matrix()
            self.assertEqual(len(a), 3)
            self.assertEqual(len(a[0]), 2)

    # Tests multiplying matrices
    def testMul(self):
        # This line mocks the users input for each time user input is required
        with mock.patch('builtins.input', side_effect=[5, 1, 5, 1, 2, 3, 4, 2, 1, 5, 5, 4, 1, 2, 3, 3]):
            a = Matrix()
            b = Matrix()
            c = a * b
            d = a * TwistedInt(2, 5)  # Tests that multiplying a Matrix by a twisted int works
            for i in range(len(c)):  # For every item in resultant
                for j in range(len(c[i])):
                    part = TwistedInt(0, a[0][0].n)  # empty twisted int to be used to add things too
                    for columns in range(len(a[0])):  # calculates the correct output for the cell
                        part = part + a[i][columns] * b[columns][j]
                    self.assertEqual(c[i][j], part, "Part should be equal")
            for i in range(len(d)):  # For each item in the matrix multiplied by a twisted int
                for j in range(len(d[i])):
                    self.assertEqual(d[i][j], a[i][j] * TwistedInt(2, 5), "Should be equal")

    # Tests the add function
    def testAdd(self):
        # This line mocks the users input for each time user input is required
        with mock.patch('builtins.input', side_effect=[5, 1, 5, 1, 2, 3, 4, 2, 5, 1, 5, 4, 1, 2, 3, 3]):
            a = Matrix()
            b = Matrix()
            c = a + b
            for i in range(len(c)):  # Checks each item in the array
                for j in range(len(c[i])):
                    self.assertEqual(c[i][j], a[i][j] + b[i][j], "Should be equal")

    # Tests some of the validation in adding matrices
    def testAddValidation(self):
        # This line mocks the users input for each time user input is required
        with mock.patch('builtins.input', side_effect=[1, 1, 5, 1, 2, 3, 5, 1, 4, 2, 3, 4, 2]):
            a = Matrix()
            b = Matrix()
            with self.assertRaisesRegex(TypeError, "The matrices can't be added as they are different sizes"):
                a + b
            with self.assertRaisesRegex(TypeError, "The type of the second argument is not a matrix"):
                a + 3

    # Tests some of the validation in multiplying matrices
    def testMultValidation(self):
        # This line mocks the users input for each time user input is required
        with mock.patch('builtins.input', side_effect=[2, 3, 5, 1, 4, 2, 3, 4, 2]):
            a = Matrix()
            with self.assertRaisesRegex(TypeError, "Please multiply a matrix by another matrix or a twisted int"):
                a * 3
            with self.assertRaisesRegex(TypeError, "The matrices can't be multiplied as they are different sizes"):
                a * a

    # tests the print method
    def testPrint(self):
        # This line mocks the users input for each time user input is required
        with mock.patch('builtins.input', side_effect=[2, 3, 5, 1, 4, 2, 3, 4, 2]):
            a = Matrix()
            # sets up a variable to record the programs output
            output = io.StringIO()
            sys.stdout = output
            print(a)
            self.assertEqual(output.getvalue(), "[[<1:5>, <4:5>, <2:5>],\n [<3:5>, <4:5>, <2:5>]]\n")

    # haven't tested all possible inputs because as inputs are twisted ints they are validated by those rules


# runs the unit tests in the file
if __name__ == '__main__':
    unittest.main()
