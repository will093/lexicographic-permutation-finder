import math

class LexPermFinder(object):

    def __init__(self, numbers):
        # numbers must be a non-empty list of numbers
        if len(numbers) > 0:
            self.numbers = numbers
        else:
            raise ValueError("Argument must contain a " 
                    "list with at least one number.")

        for number in self.numbers:
            number = float(number)
        self.numbers.sort()

    def getNthPermutation(self,n):
        # n must be an integer less than the total number
        # of permutations of 'numbers'.
        if n % 1.0 != 0:
            raise ValueError("You must specify an " 
                    "integer valued permutation")
        elif (n > math.factorial(len(self.numbers)) or n <= 0):
            raise ValueError("You must specify a permutation between "
                    "1 and %i" % math.factorial(len(self.numbers))) 

        return self.findPermutation(n-1, self.numbers)

    def findPermutation(self, n, numbers):
        # Base case
        if len(numbers) == 1:
            return numbers

        # Find first number in nth permutation
        nthPermutation = []
        indexForFirstNumber = n//math.factorial(len(numbers) - 1)
        nthPermutation.append(numbers[indexForFirstNumber])

        # Get values for recursive call
        n = n % (math.factorial(len(numbers) - 1))
        del numbers[indexForFirstNumber]

        # Recursively find the nth permutation
        nthPermutation += self.findPermutation(n, numbers)
        return nthPermutation






