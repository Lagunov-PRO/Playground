"""
Проверяем, является ли заданное число простым.
Если является, то True, если не является, то выдаём список всех его делителей.
В идеале выдать ещё и его факторизацию.
В идеале в экспонентной форме.
"""


# check_number = int(input("Enter a digit and i will check if it is a prime"))
def prime_or_divisors(number):
    upper_limit = int(number / 2 + 1)
    divisors = list(range(2, upper_limit))

    dividing_by = [divisor for divisor in divisors if number % divisor == 0]
    if not dividing_by:
        return True
    else:
        return dividing_by


# def get_factorization(prime_number_divisor, not_prime_number):
#     while not_prime_number < prime_number_divisor * 2:
#         times = 2 * prime_number_divisor
#     return times


check_number = 56
answer = prime_or_divisors(check_number)
if answer is True:
    print(check_number, 'is a prime')
else:
    prime_divisors = [x for x in answer if prime_or_divisors(x) is True]
    not_prime_divisors = [y for y in answer if prime_or_divisors(y) is not True]
    print('{} is not a prime, it has {} divisor{}:'.format(check_number, len(answer), '' if len(answer) < 2 else 's'))
    print(str(answer)[1:-1])
    if set(answer) == set(prime_divisors):
        print('All of which are prime!')
    else:
        print('Of which only those are prime:')
        print(prime_divisors)
        print('And those are not prime:')
        print(not_prime_divisors)
        # factorization = get_factorization(7, 56)
        # print(factorization)


#  TODO
#   According to Wolfram|Alpha we should add 1 in the start and the number itself to the list of divisors
