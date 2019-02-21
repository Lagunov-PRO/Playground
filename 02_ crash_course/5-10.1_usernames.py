"""
Есть список зарегистрированных имён пользователей и список незарегестрированных.
Нужно вывести список имён доступных для проектирования и список уже занятых.
Регистр не учитывается, т.е. iVan и IVAN — одно и то же.
"""
print('\nUsing list comprehensions to iterate')
current_users = ['JoHn', 'Bob', 'Alice', 'admin']
new_users = ['Alex', 'JOHN', 'aNNa', 'jOhn', 'alice', 'rob', 'HaRRy']

can_register = [new_user for new_user in new_users if new_user.lower() not in (x.lower() for x in current_users)]
already_used = [new_user for new_user in new_users if new_user.lower() in (x.lower() for x in current_users)]


# can_register_enumerated = list(enumerate(can_register, 1))
can_register_range = list(range(1, len(can_register)))
print(can_register_range)

can_register_range_zero = ['{:02d}'.format(x) for x in range(1, len(can_register))]
print(can_register_range_zero)

numbered_items = ['{:02d}. {}'.format(x, y) for x, y in enumerate(can_register, 1)]

# numbered_items = []
# for x, y in enumerate(can_register, 1):
#     numbered_item = '{number:02d}. {list_item}'.format(number = x, list_item = y)
#     numbered_items.append(numbered_item)
# print(numbered_items)


# can_register_no = ['. '.join("{}".format(x) for x in numbered) for numbered in enumerate(can_register, 1)]
# print(can_register_no)


# can_register_no = ['. '.join("{}".format(x) for x in numbered) for numbered in enumerate(can_register, 1)]
# print(can_register_no)
#
# already_used_no = ['. '.join("{}".format(x) for x in numbered) for numbered in enumerate(already_used, 1)]
# print(already_used_no)
#
print('\nCan register:\n', '\n'.join('\t{}'.format(x) for x in numbered_items))
# print('\nAlready used:\n', '\n'.join('\t{}'.format(x) for x in already_used_no))


