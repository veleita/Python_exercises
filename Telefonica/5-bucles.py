def decompose_number(num):
    prime_factors = []
    prime_num = 2
    while prime_num ** 2 <= num:
        if num % prime_num == 0:
            num //= prime_num
            prime_factors.append(prime_num)
        else:
            prime_num += 1
    if num > 1:
        prime_factors.append(num)
    return prime_factors

print(decompose_number(18))
print(decompose_number(21))
print(decompose_number(78675))


def greatest_common_divisor(a, b):
    while b:
        a, b = b, a%b
    return a

print(greatest_common_divisor(20, 15))
print(greatest_common_divisor(245, 1560))
print(greatest_common_divisor(21, 7))