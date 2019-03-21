from itertools import groupby


def unique_in_order(your_string):
    """
    >>> unique_in_order('AAAABBBCCDAABBB')
    ['A', 'B', 'C', 'D', 'A', 'B']

    >>> unique_in_order('ABBCcAD')
    ['A', 'B', 'C', 'c', 'A', 'D']

    >>> unique_in_order([1,2,2,3,3])
    [1, 2, 3]
    """
    new_list = []
    for x in range(1, len(your_string) + 1):
        if your_string[x-1:x] != your_string[x:x+1]:
            new_list.extend(your_string[x-1:x])
    return new_list


def unique_in_order_pythonic(iterable):
    """
    >>> unique_in_order_pythonic('AAAABBBCCDAABBB')
    ['A', 'B', 'C', 'D', 'A', 'B']

    >>> unique_in_order_pythonic('ABBCcAD')
    ['A', 'B', 'C', 'c', 'A', 'D']

    >>> unique_in_order_pythonic([1,2,2,3,3])
    [1, 2, 3]
    """
    result = []
    prev = None
    for char in iterable:
        if char != prev:
            result.append(char)
            prev = char
    return result
