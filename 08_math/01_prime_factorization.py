from functools import reduce
from math import sqrt, floor


def factorize_all_up_to(up_to):
    divisors = list(range(2, up_to + 1))  # Just a list of all divisors that we need to check
    prime_divisors = []
    not_prime_divisors = []
    not_prime_divisors_factorized = {}
    building_blocks = {}
    split_divisors_to_prime_and_not(divisors, prime_divisors, not_prime_divisors)
    print(prime_divisors)
    print(not_prime_divisors)

    for number in not_prime_divisors:
        get_factors(number, prime_divisors, not_prime_divisors_factorized, building_blocks)

    print(not_prime_divisors_factorized)

    print(building_blocks)

    move_factorized_to_building_blocks(not_prime_divisors_factorized, building_blocks)

    print(not_prime_divisors_factorized)
    print(building_blocks)

    divide_to_factorize(not_prime_divisors_factorized)

    print(not_prime_divisors_factorized)

    move_factorized_to_building_blocks(not_prime_divisors_factorized, building_blocks)

    print(not_prime_divisors_factorized)
    print(building_blocks)




def split_divisors_to_prime_and_not(divisors: list, prime_divisors: list, not_prime_divisors: list):

    for divisor in divisors:
        if check_if_prime(divisor):
            prime_divisors.append(divisor)
        else:
            not_prime_divisors.append(divisor)


def check_if_prime(number):
    max_divisor = floor(sqrt(number))
    for divisor in range(2, max_divisor + 1):
        if number % divisor == 0:
            return False
    return True


def split_divisors_to_prime_and_not_2(divisors: list, prime_divisors: list, not_prime_divisors: dict):

    for divisor in divisors:
        tmp = []
        for n in range(2, divisors[-1]):
            if divisor % n == 0:
                tmp.append(n)
        prime_divisors.extend(tmp) if len(tmp) == 1 else not_prime_divisors.update({divisor: tmp[0:-1]})


def get_factors(number, prime_divisors, not_prime_divisors_factorized, building_blocks):
    tmp = []
    for divisor in prime_divisors:

        if number % divisor == 0:
            tmp.append(divisor)
    if len(tmp) == 1:
        tmp = multiply_factors(number, tmp)
        building_blocks[number] = tmp
    elif reduce(lambda a, b: a * b, tmp) == number:
        building_blocks[number] = tmp
    else:
        not_prime_divisors_factorized[number] = tmp


def multiply_factors(number: int, factors: list):
    single_factor = factors[0]
    copy_factors = factors[:]

    while reduce(lambda a, b: a * b, copy_factors) != number:
        copy_factors.append(single_factor)
    return copy_factors


def move_factorized_to_building_blocks(not_prime_divisors_factorized: dict, building_blocks: dict):
    for number, factors in not_prime_divisors_factorized.items():
        if reduce(lambda a, b: a * b, factors) == number:

            building_blocks[number] = factors


def divide_to_factorize(not_prime_divisors_factorized):
    for number, factors in not_prime_divisors_factorized.items():
        new_factor = number
        for factor in factors:
            new_factor = new_factor / factor
        not_prime_divisors_factorized[number].append(int(new_factor))














if __name__ == '__main__':
    factorize_all_up_to(30)