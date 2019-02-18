n = 50
a = [True] * n
a[0] = a[1] = False
for k in range(n - 1):
    if a[k]:
        for m in range(2*k, n, k):
            a[m] = False

for k in range(n):
    if a[k]:
        print(k, '—', 'простое')
