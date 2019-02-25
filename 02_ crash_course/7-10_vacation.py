"""
Write a program that polls users about their dream
vacation . Write a prompt similar to If you could visit one place in the world,
where would you go? Include a block of code that prints the results of the poll .
"""

poll_active = True
vacation_poll = {}
while poll_active:
    name = input('What is your name? ')
    name = name.strip()
    name = name.lower()
    if name == '':
        break
    place = input('Where would you like to go? ')
    place = place.strip()
    place = place.lower()

    vacation_poll[name] = place

for name, place in vacation_poll.items():
    print('{} would like to go to {}'.format(name.title(), place.title()))
