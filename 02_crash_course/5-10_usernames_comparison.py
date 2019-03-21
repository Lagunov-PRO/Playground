#  Громоздкая итерация, неудобный вывод, лучше делать append, хотя ещё лучше всё свернуть в comprehension, см. ниже
print('Iterating over list to compare')
current_users = ['JoHn', 'Bob', 'Alice', 'admin']
new_users = ['Alex', 'JOHN', 'aNNa', 'jOhn']
current_users_lowercased = [x.lower() for x in current_users]

for new_user in new_users:
    if new_user.lower() not in current_users_lowercased:
        print(new_user, 'can register')
    else:
        print(new_user, 'is already used')

#  Наилучший способ, можно сразу вернуть список неподходящих имён
print('\nUsing list comprehensions to iterate')
current_users = ['JoHn', 'Bob', 'Alice', 'admin']
new_users = ['Alex', 'JOHN', 'aNNa', 'jOhn', 'alice', 'rob']

can_register = [new_user for new_user in new_users if new_user.lower() not in (x.lower() for x in current_users)]
already_used = [new_user for new_user in new_users if new_user.lower() in (x.lower() for x in current_users)]

print('\nCan register:\n', '\n'.join('\t{}'.format(x) for x in can_register))
print('\nAlready used:\n', '\n'.join('\t{}'.format(x) for x in already_used))


#  Используя set теряется возможно вернуть исходные значения с оригинальными регистрами
print('\n Using sets to compare')
current_users = ['JoHn', 'Bob', 'Alice', 'admin']
new_users = ['alex', 'JOHN', 'anna', 'jOhn']
current_users_lowercased = set([x.lower() for x in current_users])
new_users_lowercased = set([x.lower() for x in new_users])

already_registered = new_users_lowercased.intersection(current_users_lowercased)
can_register = new_users_lowercased.difference(current_users_lowercased)

print('{} is already used'.format(already_registered))
print('{} can register'.format(can_register))
