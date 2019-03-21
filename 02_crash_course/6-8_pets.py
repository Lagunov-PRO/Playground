nokker = {'kind': 'dog', 'owner': 'sveta'}
mikella = {'kind': 'cat', 'owner': 'sasha'}
sharik = {'kind': 'dog', 'owner': 'petya'}
tuzik = {}

pets = [nokker, mikella, sharik]

for pet in pets:
    kind = pet['kind']
    owner = pet['owner']
    print('{} owns a {}'.format(owner.title(), kind))


print()
print('Who owns a dog:')
for pet in pets:
    if pet['kind'] == 'dog':
        owner = pet['owner']
        print('\t {}'.format(owner.title()))

tuzik['kind'] = input('What pet do you have?')
tuzik['owner'] = input('What is your name?')
pets.append(tuzik)

print('Who owns a dog:')
for pet in pets:
    if pet['kind'] == 'dog':
        owner = pet['owner']
        print('\t {}'.format(owner.title()))
