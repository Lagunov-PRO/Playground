fruits = ['apples', 'bananas', 'pineapples', 'strawberry', 'lychee']
favorite_fruits = ['bananas', 'lychee', 'coconut']

print('From our list of fruits')
for favorite_fruit in favorite_fruits:
    if favorite_fruit in fruits:
        print("we have ", favorite_fruit)
    else:
        print("we don't have", favorite_fruit)

