current_users = ['JoHn', 'Bob', 'Alice', 'admin']
new_users = ['alex', 'JOHN', 'anna']
current_users_lowercased = [x.lower() for x in current_users]
for new_user in new_users:
    if new_user.lower() not in current_users_lowercased:
        print(new_user, 'can register')
    else:
        print(new_user, 'is already used')

#  TODO
#   How to check lowercased values without creating new list?
