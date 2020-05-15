'''
Let d(n) be defined as the sum of proper divisors of n (numbers less than n
which divide evenly into n). If d(a) = b and d(b) = a, where a ≠ b, then a 
and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44,
55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4,
71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''

def divisors_sum(n):
    total = 1
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            total += i
    return total


def amicable_finder(upto):
    amic = []
    for a in range(1, upto + 1):
        b = divisors_sum(a)
        divs_b = divisors_sum(b)
        if divs_b == a and a != b:
            amic.append(a)
            print(f'- found amicable! d({a}) = {b}, d({b}) = {divs_b}')
    return sum(amic)

print()
upto = int(input('Calculate the sum of amicable nums up to: '))
total = amicable_finder(upto)

print(f'\nSum of amicable nums under {upto} = {total}')
