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
    print(prime_factors)

decompose_number(18)
decompose_number(21)
decompose_number(78675)