'''
Surprisingly there are only three numbers that can be written as the
sum of fourth powers of their digits:

1634 = 14 + 64 + 34 + 44
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44

As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth
powers of their digits.
'''

def is_self_power(num):
    digits = [int(x) for x in str(num)]
    summ = 0
    for digit in digits:
        summ += (digit ** 5)
    return num == summ


def main():
    found = 0
    for num in range(0, 10000000):
        if is_self_power(num):
            print(f'Found one num: {num}')
            found += num
    print(f'total {found}')


if __name__ == "__main__":
    main()