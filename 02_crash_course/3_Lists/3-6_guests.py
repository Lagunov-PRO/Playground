guests = ['венера', 'евгений', 'дамир', 'дамир', 'артур', 'айрат']

print(len(guests))

guests.insert(0, 'ленар')
guests.append('руслан')
guests.insert(len(guests) // 2, 'аида')

print()
print(len(guests), "гостей приглашено")
guest_index = 0
for guest in guests:
    guest_index += 1
    greeting = 'приглашён'
    last_letter = guest[-1]
    if last_letter == 'а':
        greeting = 'приглашена'
    print('{:02d}. {} {}'.format(guest_index, guest.title(), greeting))

print()

guests_invited = len(guests)
have_table_for = 4
for guest in range(guests_invited - have_table_for):
    removed_guest = guests.pop()
    greeting = 'приглашён'
    last_letter = removed_guest[-1]
    if last_letter == 'а':
        greeting = 'приглашена'
    print('Мне очень жаль, но {} больше не {}'.format(removed_guest.title(), greeting))

guests_left = len(guests)
print('Осталось гостей: {}'.format(guests_left))

guests_string = str()  # Пустая строка
for guest in guests:
    guests_string += ('{}, '.format(guest.title()))  # Пустая строка + элементы по списку

print(guests_string[:-2])  # Отрубаем последние два символа
