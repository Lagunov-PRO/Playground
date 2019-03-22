users = ['alex', 'anna', 'emily', 'admin']
if users:
    for user in users:
        if user == 'admin':
            print('Hello, sir', user)
        else:
            print('Whats up,', user)
else:
    print('no users')


print(users.pop())
print(users.pop())
print(users.pop())
print(users.pop())

