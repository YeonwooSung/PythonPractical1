import unittest
from unittest import mock
import io
import sys
from unittest.mock import patch

from newTwist import *

class NewTwistTests(unittest.TestCase):

    def testInit(self):
        a = NewTwist(2, 5)
        self.assertEqual(2, a.val, "value should be 2")
        self.assertEqual(5, a.n, "n value should be 5")
        self.assertFalse(a.addExists, "The add operator should not be defined yet.")
        self.assertFalse(a.multExists, "The mult operator should not be defined yet.")
        self.assertEqual(0, a.openBrackets, "The number of open brackets should be 0.")

    def testInitValidation(self):
        with self.assertRaisesRegex(ValueError, "The range of the value should be greater than 0."):
            NewTwist(2, -5)

    def testPrintOverwrite(self):
        output = io.StringIO()
        sys.stdout = output

        a = NewTwist(2, 5)
        print(a)

        self.assertEqual("<2:5>\n", output.getvalue(), "The format of the output should be equal to this.")

    def testEqualsNewTwist(self):
        a = NewTwist(2, 5)
        b = NewTwist(3, 5)
        c = NewTwist(2, 5)

        self.assertFalse(a == b, "Should not be equal")
        self.assertTrue(a == c, "Should be equal")
        self.assertTrue(a == a, "Should be equal")

    def testEqulasValidation(self):
        with self.assertRaisesRegex(TypeError, "The type of the second argument is not the NewTwist!"):
            NewTwist(2, 5) == 2
        with self.assertRaisesRegex(ValueError, "The value n of the two objects should be same!"):
            NewTwist(2, 5) == NewTwist(2, 6)

    def testNotEqualsNewTwist(self):
        a = NewTwist(2, 5)
        b = NewTwist(3, 5)
        c = NewTwist(2, 5)

        self.assertTrue(a != b, "Should not be equal")
        self.assertFalse(a != c, "Should be equal")
        self.assertFalse(a != a, "Should be equal")

    def testAddNewTwist(self):
        with mock.patch('builtins.input', side_effect=['a','+','b','%','n', 'q']):
            a = NewTwist(2, 5)
            b = NewTwist(3, 5)
            c = a + b
            self.assertEqual(c, NewTwist(5, 5))

    def testMulNewTwist(self):
        with mock.patch('builtins.input', side_effect=['a','*','b','%','n','q']):
            a = NewTwist(2, 5)
            b = NewTwist(3, 5)
            c = a * b
            self.assertEqual(c, NewTwist(6, 5))


if __name__ == '__main__':
    unittest.main()
