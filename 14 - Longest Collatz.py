'''
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?
'''

def collatz_seq(n):
    i = 1

    while n > 1:
        i += 1
        if n % 2 == 0:
            n /= 2
        else:
            n = (n * 3) + 1
    return i

def largest_collatz(upto):
    largest = 1
    largest_terms = 0
    for num in range(1, upto + 1):
        terms = collatz_seq(num)
        if terms > largest_terms:
            largest = num
            largest_terms = terms
    return largest

print(collatz_seq(837799))
