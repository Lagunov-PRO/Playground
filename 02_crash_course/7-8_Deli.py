"""
Make a list called sandwich_orders and fill it with the names of vari-
ous sandwiches . Then make an empty list called finished_sandwiches . Loop
through the list of sandwich orders and print a message for each order, such
as I made your tuna sandwich. As each sandwich is made, move it to the list
of finished sandwiches . After all the sandwiches have been made, print a
message listing each sandwich that was made .
"""
sandwich_orders = ['ham', 'turkey', 'bmt', 'tuna', 'pastrami', 'pastrami', 'pastrami']
finished_sandwiches = []

not_available = 'pastrami'
print('Sorry {} sandwich is not available'.format(not_available))

while not_available in sandwich_orders:
    sandwich_orders.remove(not_available)

while sandwich_orders:
    making_sandwich = sandwich_orders.pop()
    finished_sandwiches.append(making_sandwich)
    print('Cooking {} sandwich'.format(making_sandwich))
