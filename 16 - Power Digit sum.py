def digit_sum(number):
    digits = [int(x) for x in str(number)]
    return sum(digits)

print(digit_sum(2**1000))