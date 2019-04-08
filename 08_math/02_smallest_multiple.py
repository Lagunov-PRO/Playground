from functools import reduce


def new_smallest_multiple():

    divisors_list = list(range(2, 21))
    prime_divisors_list = [2, 3, 5, 7, 11, 13, 17, 19]
    not_primes = {4: [2], 6: [2, 3], 8: [2], 9: [3], 10: [2, 5], 12: [2, 3], 14: [2, 7], 15: [3, 5], 16: [2], 18: [2, 3], 20: [2, 5]}
    all_divisors_list = [2, 2, 2, 2, 3, 3, 5, 7, 11, 13, 17, 19]

    prime_divisors_product = reduce(lambda a, b: a * b, all_divisors_list)
    print(prime_divisors_product)
    for divisor in divisors_list:
        if prime_divisors_product % divisor != 0:
            print(divisor, prime_divisors_product % divisor)




new_smallest_multiple()