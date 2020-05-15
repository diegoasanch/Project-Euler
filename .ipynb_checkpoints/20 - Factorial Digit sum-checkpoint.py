def digit_sum(number):
    digits = [int(x) for x in str(number)]
    return sum(digits)

    
def factorial(number):
    fact = 1
    for i in range(1, number + 1):
        fact *= i
    return fact


fact = factorial(100)
print(fact)
d_sum = digit_sum(fact)
print(d_sum)