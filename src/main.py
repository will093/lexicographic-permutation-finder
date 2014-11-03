import InputReader
from LexPermFinder import LexPermFinder

numbers = InputReader.getNumbers()
try:
    permutation = InputReader.getPermutation()
    lexPermFinder = LexPermFinder(numbers)
except ValueError as e:
    print e.value

print "Permutation number %i is:" % permutation
print lexPermFinder.getNthPermutation(permutation)
