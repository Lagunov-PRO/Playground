from app.months import list_of_months

print(list_of_months(3))

months = [((month % 12) + 1) for month in range(2, 14)]

print(months)

squares = [value**2 for value in range(10)]

print(squares)
roots = []
for square in squares:
    roots.append(square**0.5)
print(roots)


odd_numbers = [k * 2 + 1 for k in range(25)]
print(odd_numbers[0:40])

multiples_of_three = [k * 3 for k in range(1, 31)]
print(multiples_of_three)

list_of_cubes = [k ** 3 for k in range(1, 11)]
print(list_of_cubes)
