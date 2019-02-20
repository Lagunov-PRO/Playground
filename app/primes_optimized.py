# number = int(input("Enter a digit and i will check if it is a prime"))


def check_prime(number):
    upper_limit = int(number / 2 + 1)
    print(upper_limit)
    divisors = list(range(2, upper_limit))
    print(divisors)
    # remainders = [number % divisor for divisor in divisors]
    for divisor in divisors:
        if number % divisor == 0:
            return False
    return True


check_number = 4
answer = check_prime(check_number)
print(check_number, answer)
