"""
Есть список зарегистрированных имён пользователей и список незарегестрированных.
Нужно вывести список имён доступных для проектирования и список уже занятых.
Регистр не учитывается, т.е. iVan и IVAN — одно и то же.
"""
print('\nUsing list comprehensions to iterate')
current_users = ['JoHn', 'Bob', 'Alice', 'admin']
new_users = ['Alex', 'JOHN', 'aNNa', 'jOhn', 'alice', 'rob', 'HaRRy', 'harry', 'HaRRy']

#  Removing possible duplicates from new_users list converting to set() and  back to list()
new_users = list(set(new_users))

can_register = [new_user for new_user in new_users if new_user.lower() not in (x.lower() for x in current_users)]
already_used = [new_user for new_user in new_users if new_user.lower() in (x.lower() for x in current_users)]


can_register_numbered = ['{:02d}. {}'.format(x, y) for x, y in enumerate(can_register, 1)]
already_used_numbered = ['{:02d}. {}'.format(x, y) for x, y in enumerate(already_used, 1)]

print('\nCan register:')
print('\n'.join('\t{}'.format(x) for x in can_register_numbered))
print('\nAlready used:')
print('\n'.join('\t{}'.format(x) for x in already_used_numbered))
