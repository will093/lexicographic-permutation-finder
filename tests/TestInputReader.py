from nose.tools import *
import unittest
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

if __name__ == '__main__':
    unittest.main()




