"""
A=[1,2,3,4,5,7,12,9,6,-5,-7,-12,2]
B=[0 if x<0 else x**2 for x in A if x%2==0]
print(B)
Output:
[4, 16, 144, 36, 0, 4]﻿
"""
# Неправильный вариант
A = [1, 2, 3, 4, 5, 7, 12, 9, 6, -5, -7, -12, 2]
B = []
for x in A:
    if x % 2 == 0:
        if x < 0:
            B.append(0)
        else:
            B.append(x**2)
print(B)

# Правильный вариант
A = [1, 2, 3, 4, 5, 7, 12, 9, 6, -5, -7, -12, 2]
print(A)
B_0 = [x**2 if x >= 0 and x % 2 == 0 else 0 for x in A]
print(B_0)