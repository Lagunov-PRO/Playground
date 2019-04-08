

def test():
    prime_factorization = {}
    for factorization in not_prime_divisors:
        number = factorization[-1]
        all_factors = factorization[0:-1]
        prime_factors = []
        for n in all_factors:
            if n in prime_divisors:
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


print(split_divisors_to_prime_and_not(20))

#  TODO: make a cycle