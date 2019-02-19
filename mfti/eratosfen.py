upper_limit = 1_000
A = [True] * upper_limit
A[0] = A[1] = False  # 0 and 1 are not primes
numbers = [k for k in range(upper_limit)]
# print(numbers)
for k in range(upper_limit - 1):
    rejected = []
    if A[k]:
        for m in range(2*k, upper_limit, k):
            rejected.append(m)
            A[m] = False
    if rejected:
        print('Делитель {}, отброшено {}'.format(k, len(rejected)))

primes = [k for k in range(upper_limit) if A[k]]

print(primes)
print(len(primes))


