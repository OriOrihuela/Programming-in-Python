# Function to discover if an the input number
# is prime or not. If it is, the result will be
# True. If not, False.

def isPrime(x):
    if x in (0, 1):
        return False
    for i in range(2, int(x ** 0.5)+1):
        if x % i == 0:
            return False
    return True


if __name__ == "__main__":

    # CASOS TEST #

    if isPrime(6):
        print("6 Is prime")
    else:
        print("6 is not prime")

    if isPrime(73):
        print("73 is prime")
    else:
        print("73 is not prime")

    if isPrime(564):
        print("564 is prime")
    else:
        print("564 is not prime")

    if isPrime(11):
        print("11 is prime")
    else:
        print("11 is not prime")

    if isPrime(67):
        print("67 is prime")
    else:
        print("67 is not prime")

    if isPrime(88):
        print("88 is prime")
    else:
        print("88 is not prime")

    if isPrime(233):
        print("233 is prime")
    else:
        print("233 is not prime")

    if isPrime(1):
        print("1 is prime")
    else:
        print("1 is not prime")

    if isPrime(2):
        print("2 is prime")
    else:
        print("2 is not prime")

    if isPrime(0):
        print("0 is prime")
    else:
        print("0 is not prime")

    