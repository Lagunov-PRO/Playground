"""
7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of
pizza toppings until they enter a 'quit' value . As they enter each topping,
print a message saying you’ll add that topping to their pizza .
"""
active = True
user_toppings = []
print('Which toppings do you like? ')
while active:
    user_topping = input()
    if user_topping == '':
        active = False
    else:
        user_toppings.append(user_topping)
print(user_toppings)
