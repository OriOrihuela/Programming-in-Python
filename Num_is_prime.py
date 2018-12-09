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

    assert not isPrime(6)
    assert isPrime(73)
    assert not isPrime(564)
    assert isPrime(11)
    assert isPrime(67)
    assert not isPrime(88)
    assert isPrime(233)
    assert not isPrime(1)
    assert isPrime(2)
    assert not isPrime(0)

    
