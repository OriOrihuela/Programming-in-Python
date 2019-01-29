''' Creating a function that sums prime numbers between some proposed numbers.
The last number proposed it is not required into the sumatory. '''

def sumPrimeNumbers(initialNumber, finalNumber):
    sumatory = 0
    numberToBeAdded = initialNumber
    
    if numberToBeAdded < 2:
        return "Cannot be done, the number is not a prime number."
    
    while numberToBeAdded < finalNumber:
        divisor = 2
        while (divisor < numberToBeAdded) and (numberToBeAdded % divisor != 0):
            divisor += 1
        if divisor == numberToBeAdded:
            sumatory += numberToBeAdded
        numberToBeAdded += 1
    
    return sumatory


if __name__ == "__main__":
    

    # TEST CASES #

    assert sumPrimeNumbers(2, 30) == 129
    assert sumPrimeNumbers(2, 100) == 1060