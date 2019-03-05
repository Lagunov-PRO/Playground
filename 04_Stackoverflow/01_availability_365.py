"""
I have a column in a data named availability_365 the column contains numbers between 0 and 365. I want a python
code that would categorise the numbers to fall between 1 and 3. So if the number is between 0 and 122 it should be
converted to 1, numbers 123-245 should be converted to 2 and 245-365 be converted to 3. Would appreciated any help
please, thanks.
"""


def convert_365(availability_365: list, a=1, b=2, c=3):
    converted = []
    for number in availability_365:
        if number < 123:
            converted.append(a)
        elif 122 < number <= 245:
            converted.append(b)
        elif number >= 246:
            converted.append(c)
    return converted


availability_365 = list(range(0, 366))
a, b, c = 1, 2, 3
print(convert_365(availability_365), a, b, c)

print(convert_365(availability_365)[0] == a)
print(convert_365(availability_365)[122] == a)
print(convert_365(availability_365)[123] == b)
print(convert_365(availability_365)[245] == b)
print(convert_365(availability_365)[246] == c)
print(convert_365(availability_365)[365] == c)

