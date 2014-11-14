def promptForNumber():
    return raw_input("Enter a number: ")

def promptForPermutation():
    return raw_input("\nEnter the permutation you wish to find: ")

def getNumbers(inputFunction = promptForNumber):
    numbers = []
    print ("\nEnter the numbers you wish to find " 
           "a permutation of, or 'q' to finish.\n")
    while True:
        number = inputFunction()

        if number == "q":
            if len(numbers) == 0:
                print "You must enter at least 1 number..."
                continue
            else:
                return numbers
        else:
            try:
                numbers.append(float(number))
            except ValueError:
                print "You must enter a numerical value..."


def getPermutation(inputFunction = promptForPermutation):

    while True:
        permutation = inputFunction()
        if permutation.isdigit() == False or int(permutation) <= 0:
            print "You must enter a positive integer value"
            continue
        return int(permutation)
