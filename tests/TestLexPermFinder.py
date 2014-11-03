import unittest
from nose.tools import *
from mock import Mock

from LexPermFinder import LexPermFinder

class TextLexPerm(unittest.TestCase):

    def testShouldThrowIfPermutationTooLarge(self):
        numbers = [1,2,3,4]
        lexPerm = LexPermFinder(numbers)
        self.assertRaises(ValueError, 
                lexPerm.getNthPermutation, 25)

    def testShouldThrowIfPermutationNonPositive(self):
        numbers = [1,2,3,4]
        lexPerm = LexPermFinder(numbers)
        self.assertRaises(ValueError, 
                lexPerm.getNthPermutation, 0)

    def testShouldThrowIfPermutationIsFloat(self):
        numbers = [1,2,3,4]
        lexPerm = LexPermFinder(numbers)
        self.assertRaises(ValueError, 
                lexPerm.getNthPermutation, 3.22)

    def testShouldThrowIfNumbersLengthIsZero(self):
        numbers = []
        self.assertRaises(ValueError, LexPermFinder, numbers) 

    def testShouldThrowIfNumbersContainsInvalidTypes(self):
        numbers = ['s', 3]
        self.assertRaises(ValueError, LexPermFinder, numbers) 

    def testShouldGetValidPermutationOfSortedPositives(self):
        numbers = [1,2,3,4]
        lexPerm = LexPermFinder(numbers)
        result = lexPerm.getNthPermutation(13)
        expected = [3,1,2,4]
        self.assertEqual(result, expected)
        

    def testShouldGetValidPermutationOf1Number(self):
        numbers = [1]
        lexPerm = LexPermFinder(numbers)
        result = lexPerm.getNthPermutation(1)
        expected = [1]
        self.assertEqual(result, expected)


    def testShouldGetValidPermutationOfAnyUnsortedNumbers(self):
        numbers = [-5437, 8.3,0]
        lexPerm = LexPermFinder(numbers)
        result = lexPerm.getNthPermutation(3)
        expected = [0,-5437,8.3]
        self.assertEqual(result, expected)

    def testShouldGetFirstPermutationOfAnyUnsortedNumbers(self):
        numbers = [-5437, 8.3, 0]
        lexPerm = LexPermFinder(numbers)
        result = lexPerm.getNthPermutation(1)
        expected = [-5437, 0, 8.3]
        self.assertEqual(result, expected)
   
    def testShouldGetLastPermutationOfAnyUnsortedNumbers(self):
        numbers = [-5437, 8.3,0]
        lexPerm = LexPermFinder(numbers)
        result = lexPerm.getNthPermutation(6)
        expected = [8.3, 0, -5437]
        self.assertEqual(result, expected)
