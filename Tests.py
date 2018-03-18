import unittest
import io
import sys
from unittest.mock import patch

from twistedint import *


class TwistedIntTests(unittest.TestCase):

    # Tests the creation of twisted ints
    def testInit(self):
        a = TwistedInt(2, 5)
        self.assertEqual(2, a.val, "value should be 2")
        self.assertEqual(5, a.n, "value should be 5")

    # Tests the validation in setting up the twisted int
    def testInitValidation(self):
        with self.assertRaisesRegex(ValueError, "The range of the value should be greater than 0."):
            TwistedInt(2, -5)
        with self.assertRaisesRegex(ValueError, "The value of the TwistedInt should be in the range of 0 ~ n-1"):
            TwistedInt(3, 2)
        with self.assertRaisesRegex(ValueError, "The value of the TwistedInt should be in the range of 0 ~ n-1"):
            TwistedInt(-5, 4)

    # Tests that the twisited ints are printed correctly
    def testPrintOverwrite(self):
        # sets up variable to record the programs output
        output = io.StringIO()
        sys.stdout = output

        a = TwistedInt(2, 5)
        print(a)

        self.assertEqual("<2:5>\n", output.getvalue(), "Should be overwritten in this format")

    # Tests the addition of two twisted ints
    def testAddition(self):
        a = TwistedInt(3, 5)
        b = TwistedInt(4, 5)
        c = TwistedInt(15,16)

        self.assertEqual(TwistedInt((a.val + a.val) % a.n, a.n), a + a, "Should be equal")
        self.assertEqual(TwistedInt((a.val + b.val) % a.n, a.n), a + b, "Should be equal")
        self.assertEqual(TwistedInt((c.val + c.val) % c.n, c.n), c + c, "Should be equal")

    # Tests the validation of adding twisted ints
    def testAdditionValidation(self):
        a = TwistedInt(3, 5)
        b = TwistedInt(3, 4)
        with self.assertRaisesRegex(TypeError, "The type of the second argument is not the TwistedInt!"):
            a + 3
        with self.assertRaisesRegex(ValueError, "The value n of the two objects should be same!"):
            a + b

    # Tests multiplying twisted ints
    def testMult(self):
        a = TwistedInt(3, 5)
        b = TwistedInt(4, 5)
        self.assertEqual(TwistedInt((a.val + b.val + (a.val * b.val)) % b.n, a.n), a * b, "Objects are not multiplying correctly")
        self.assertEqual(TwistedInt((a.val + a.val + (a.val * a.val)) % a.n, a.n), a * a, "Objects are not multiplying correctly")
        self.assertEqual(TwistedInt((b.val + b.val + (b.val * b.val)) % b.n, b.n), b * b, "Objects are not multiplying correctly")

    # Tests the validation of multiplying twisted ints
    def testMultValidation(self):
        a = TwistedInt(3, 5)
        b = TwistedInt(4, 16)
        with self.assertRaisesRegex(TypeError, "The type of the second argument is not the TwistedInt!"):
            a * 2
        with self.assertRaisesRegex(ValueError, "The value n of the two objects should be same!"):
            a * b

    # Tests the equality overridden method
    def testEqualsOverride(self):
        a = TwistedInt(3, 5)
        b = TwistedInt(4, 5)
        c = TwistedInt(3, 5)
        self.assertTrue(a == a, "Should be equal by ==")
        self.assertTrue(a == c, "Should be comparable by ==")
        self.assertFalse(a == b, "Should not be equal")

    # Tests the do not equals overridden method
    def testNotEqualsOverride(self):
        a = TwistedInt(3, 5)
        b = TwistedInt(4, 5)
        c = TwistedInt(3, 5)
        self.assertTrue(a != b, "Should not be equal")
        self.assertFalse(a != a, "Should be equal")
        self.assertFalse(a != a, "Should not be equal")


# Runs all the tests in this file
if __name__ == '__main__':
    unittest.main()
