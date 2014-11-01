import unittest
from nose.tools import *
from mock import Mock

import InputReader

class TestInputReader(unittest.TestCase):
    
    # tests for getPermutation.

    def testIntPermutationsShouldBeAccepted(self):
        permutation = InputReader.getPermutation(lambda: "5")
        expected = 5
        self.assertEqual(permutation, expected)

    def testFloatPermutationsShouldNotBeAccepted(self):
        permutation = InputReader.getPermutation(lambda: "5.5")
        expected = -1
        self.assertEqual(permutation, expected)

    def testStringPermutationsShouldNotBeAccepted(self):
        permutation = InputReader.getPermutation(lambda: "wrong")
        expected = -1
        self.assertEqual(permutation, expected)

    def testZeroPermutationShouldNotBeAccepted(self):
        permutation = InputReader.getPermutation(lambda: "0")
        expected = -1
        self.assertEqual(permutation, expected)

    def testNegativePermutationShouldNotBeAccepted(self):    
        permutation = InputReader.getPermutation(lambda: "-10")
        expected = -1
        self.assertEqual(permutation, expected)

    # tests for getNumbers.

    def testIntNumbersShouldBeAccepted(self):
        inputFunction = Mock(side_effect = ['4','5','6','q'])
        numbers = InputReader.getNumbers(inputFunction)
        expected = [4, 5, 6]
        self.assertEqual(numbers, expected)

    
    def testDoubleNumbersShouldBeAccepted(self):
        inputFunction = Mock(side_effect = ['4.3','5.6','6.9','q'])
        numbers = InputReader.getNumbers(inputFunction)
        expected = [4.3, 5.6, 6.9]
        self.assertEqual(numbers, expected)

    
    def testNonPositiveNumbersShouldBeAccepted(self):
        inputFunction = Mock(side_effect = ['-3','-1','0','q'])
        numbers = InputReader.getNumbers(inputFunction)
        expected = [-3, -1, 0]
        self.assertEqual(numbers, expected)

    
    def testNoNumbersShouldNotBeAccepted(self):
        inputFunction = Mock(side_effect = ['q','4','5','6','q'])
        numbers = InputReader.getNumbers(inputFunction)
        expected = [4, 5, 6]
        self.assertEqual(numbers, expected)

    
    def testInvalidStringsShouldNotBeAccepted(self):
        inputFunction = Mock(side_effect = ['3','fsf','Q','5','.-3','q'])
        numbers = InputReader.getNumbers(inputFunction)
        expected = [3, 5]
        self.assertEqual(numbers, expected)
if __name__ == '__main__':
    unittest.main()




