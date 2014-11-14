import InputReader
from LexPermFinder import LexPermFinder

numbers = InputReader.getNumbers()
try:
    permutation = InputReader.getPermutation()
    lexPermFinder = LexPermFinder(numbers)
except ValueError as e:
    print e.value

print "\nPermutation number %i is:\n" % permutation
print lexPermFinder.getNthPermutation(permutation)
print ""
