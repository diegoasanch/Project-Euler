def self_power(upto):
    total = 0
    for i in range(1, upto + 1):
        total += i ** i
    return total

self_1000 = self_power(1000)
print(str(self_1000)[-10:])