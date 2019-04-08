from functools import reduce
from math import sqrt, floor


def factorize_all_up_to(up_to):
    divisors = list(range(2, up_to + 1))  # Just a list of all divisors that we need to check
    prime_divisors = []
    not_prime_divisors = []
    remove_all_primes_from_list(divisors, prime_divisors, not_prime_divisors)
    print(prime_divisors)
    print(not_prime_divisors)


def remove_all_primes_from_list(divisors: list, prime_divisors: list, not_prime_divisors: list):

    for divisor in divisors:
        if check_if_prime(divisor):
            prime_divisors.append(divisor)
        else:
            not_prime_divisors.append(divisor)


def split_divisors_to_prime_and_not(divisors_list):

    prime_divisors = []
    not_prime_divisors = []
    for divisor in divisors_list:
        tmp = []
        for n in range(2, 10):
            if divisor % n == 0:
                tmp.append(n)
        prime_divisors.extend(tmp) if len(tmp) == 1 else not_prime_divisors.append(tmp)
    return prime_divisors, not_prime_divisors


def check_if_prime(number):
    max_divisor = floor(sqrt(number))
    for divisor in range(2, max_divisor + 1):
        if number % divisor == 0:
            return False
    return True




if __name__ == '__main__':
    factorize_all_up_to(100)