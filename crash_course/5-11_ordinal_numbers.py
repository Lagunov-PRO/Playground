numbers = list(range(1, 10))
print(numbers)

ordinal_numbers = []

for number in numbers:
    if number == 1:
        ordinal_numbers.append('1st')
    elif number == 2:
        ordinal_numbers.append('2nd')
    elif number == 3:
        ordinal_numbers.append('3rd')
    else:
        ordinal_numbers.append(str(number) + 'th')
print(ordinal_numbers)
