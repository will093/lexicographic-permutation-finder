def getPermutation(inputFunction):
    permutation = inputFunction()

    if permutation.isdigit() == False:
        return -1

    if permutation == '0':
        return -1

    return int(permutation)
    
