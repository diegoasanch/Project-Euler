'''
The number, 197, is called a circular prime because all rotations of the 
digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 
71, 73, 79, and 97.

How many circular primes are there below one million?
'''

def is_prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            break
    else:
        return True
    return False


def is_circular(num):
    pass


def primes(upto):
    for i in range(1, upto + 1):
        if is_prime(i):
            print(f'prime! {i}')