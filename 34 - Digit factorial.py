'''
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial
of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
'''

def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact


def is_self_fact(num):
    digits = [int(x) for x in str(num)]
    fact_sum = 0
    for digit in digits:
        fact_sum += factorial(digit)
    return num == fact_sum

def main():

    total = 0
    for num in range(3, 1000000):
        if is_self_fact(num):
            print(f'  - self factorial: {num}')
            total += num
    print(f'\nSelf factorial sum: {total}')
    

if __name__ == "__main__":
    main()