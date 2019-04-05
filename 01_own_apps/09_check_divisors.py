import itertools
from functools import reduce


def check_divisors(number):

    div_by_list = []
    number = str(number)
    divisible_by_2 = int(number[-1]) % 2 == 0
    divisible_by_3 = sum(int(x) for x in list(number)) % 3 == 0
    divisible_by_4 = int(number[-2:]) % 4 == 0
    divisible_by_5 = int(number[-1]) == 5 or int(number[-1]) == 0
    divisible_by_6 = divisible_by_2 and divisible_by_3
    divisible_by_8 = int(number[-3:]) % 8 == 0
    divisible_by_9 = sum(int(x) for x in list(number)) % 9 == 0
    divisible_by_10 = int(number[-1]) == 0

    div_by_list.append(divisible_by_2)
    div_by_list.append(divisible_by_3)
    div_by_list.append(divisible_by_4)
    div_by_list.append(divisible_by_5)
    div_by_list.append(divisible_by_6)
    div_by_list.append(divisible_by_8)
    div_by_list.append(divisible_by_9)
    div_by_list.append(divisible_by_10)

    div_by = {
        2: divisible_by_2,
        3: divisible_by_3,
        4: divisible_by_4,
        5: divisible_by_5,
        6: divisible_by_6,
        8: divisible_by_8,
        9: divisible_by_9,
        10: divisible_by_10,
    }

    div_check_list = div_by.values()
    div_list = div_by.keys()

    divisors_check_combinations = list(itertools.chain.from_iterable(itertools.combinations(div_check_list, r) for r in range(len(div_check_list) + 1)))
    divisors_combinations = list(itertools.chain.from_iterable(itertools.combinations(div_list, r) for r in range(len(div_list) + 1)))
    for divisors, combination in zip(divisors_combinations, divisors_check_combinations):
        if divisors:
            div = reduce(lambda a, b: a * b, divisors)
            check = reduce(lambda a, b: a and b, combination)
            div_by[div] = check

    # return list(zip(divisors_combinations, divisors_check_combinations))
    return div_by


# print(largest_prime_factor(600851475143))
print(check_divisors(518400))
