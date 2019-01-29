'''Define a function isPrime/is_prime() that takes one integer argument and returns true/True or false/False 
depending on if the integer is a prime.
Per Wikipedia, a prime number (or a prime) is a natural number greater than 1 that has no positive divisors 
other than 1 and itself.'''


def is_prime(num):
  divisor = 2
  if num < 2:
      return False
  while (divisor < num) and (num % divisor != 0):
      divisor = divisor + 1
  if num == divisor:
      return True
  else:
      return False


if __name__ == "__main__":
    

    # TEST CASES #

    assert is_prime(13) == True
    assert is_prime(757) == True
    assert is_prime(919) == True
    assert is_prime(0) == False
    assert is_prime(1) == False
    assert is_prime(2) == True
    assert is_prime(77) == False
    assert is_prime(54) == False
    assert is_prime(865) == False