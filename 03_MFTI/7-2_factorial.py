
def factorial(n):
    assert n >= 0, 'No factorial for negative'
    if n == 0:
        return 1
    return factorial(n - 1) * n


print(factorial(10))
