def getPermutation(inputFunction):
    permutation = inputFunction()

    if permutation.isdigit() == False:
        return -1

    if permutation == '0':
        return -1

    return int(permutation)
    
def getNumbers(inputFunction):
    numbers = []

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


