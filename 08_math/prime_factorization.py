from functools import reduce


def prime_factorization(up_to):
    divisors_list = list(range(2, up_to + 1))  # Just a list of all divisors that we need to check

    prime_divisors_list = []
    not_prime_factorization = []
    for divisor in divisors_list:
        tmp = []
        for n in range(2, divisor + 1):
            if divisor % n == 0:
                tmp.append(n)
        prime_divisors_list.append(*tmp) if len(tmp) == 1 else not_prime_factorization.append(tmp)
    prime_factorization = {}
    for factorization in not_prime_factorization:
        number = factorization[-1]
        all_factors = factorization[0:-1]
        prime_factors = []
        for n in all_factors:
            if n in prime_divisors_list:
                prime_factors.append(n)
        prime_factorization[number] = prime_factors

    for number, factors in prime_factorization.items():
        if len(factors) == 1:
            while reduce(lambda a, b: a * b, factors) != number:
                factors.append(factors[0])

    building_blocks = {}
    for number, factors in prime_factorization.items():
        if reduce(lambda a, b: a * b, factors) == number:
            building_blocks[number] = factors

    print(building_blocks)

    for number, factors in prime_factorization.items():
        factors_product = reduce(lambda a, b: a * b, factors)
        if factors_product != number:
            factors.append(int(number / factors_product))

    for number, factors in prime_factorization.items():
        for n in factors:
            if n in building_blocks.keys():
                factors.remove(n)
                factors.extend(building_blocks[n])
                

    return prime_factorization


print(prime_factorization(1000))



