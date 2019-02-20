language_poll = {
    'alex': 'python',
    'ken': 'c++',
    'ben': 'rust',
    'karen': 'java',
    'karen2': 'python',
    'jim': 'abap',
    'bob': 'b',
}

for name in language_poll:
    print(name)

print()

for lang in sorted(set(language_poll.values())):
    print(lang)

print()

for name, lang in language_poll.items():
    if lang == 'abap':
        lang = lang.upper()
    else:
        lang = lang.title()
    print(name.title(), lang)

print()

if 'python' in language_poll.values():
    print('OK')

print()

list_lang = ['c++', 'python']
for lang in list_lang:
    if lang in language_poll.values():
        print("Thank God {} is here".format(lang.title()))

