def isPrime(x):
    """
    Checks whether the given
    number x is prime or not
    """

    if x == 2: return True

    if not x % 2: return False

    for i in range(3, int(x**0.5)+1, 2):
        if x % i == 0:
            return False

    return True


def generatePrime(currentPrime):
    """
    Returns the next prime
    after the currentPrime
    """

    newPrime = currentPrime + 1

    while True:

        if not isPrime(newPrime):
            newPrime += 1
        else:
            break

    return newPrime


def main():

    currentPrime = 2

    while True:

        answer = input('Would you like to see the next prime? (Y/N) ')

        if answer.lower().startswith('y'):
            print(currentPrime)
            currentPrime = generatePrime(currentPrime)

        else:
            break

if __name__ == '__main__':
	main()
