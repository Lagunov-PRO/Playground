# check_number = int(input("Enter a digit and i will check if it is a prime"))
def primes_or_remainders(number):
    upper_limit = int(number / 2 + 1)
    divisors = list(range(2, upper_limit))

    dividing_by = [divisor for divisor in divisors if number % divisor == 0]
    if not dividing_by:
        return True
    else:
        return dividing_by


def get_factorization(prime_number_divisor, not_prime_number):
    while not_prime_number < prime_number_divisor * 2:
        times = 2 * prime_number_divisor
    return times


check_number = 56
answer = primes_or_remainders(check_number)
if answer is True:
    print(check_number, 'is a prime')
else:
    prime_divisors = [x for x in answer if primes_or_remainders(x) is True]
    not_prime_divisors = [y for y in answer if primes_or_remainders(y) is not True]
    print('{} is not a prime, it has {} divisor{}:'.format(check_number, len(answer), '' if len(answer) < 2 else 's'))
    print(str(answer)[1:-1])
    if set(answer) == set(prime_divisors):
        print('All of which are prime!')
    else:
        print('Of which only those are prime:')
        print(prime_divisors)
        print('And those are not prime:')
        print(not_prime_divisors)
        factorization = get_factorization(7, 56)
        print(factorization)
