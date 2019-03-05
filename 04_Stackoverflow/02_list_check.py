#
# original_list = ['apples', 'oranges', 'grapes', 'oranges']
# checking_for = ['apples', 'oranges']
#
# check = any(x not in checking_for for x in original_list)
#
# print(check)
#
# original_list = ['apples', 'oranges', 'grapes', 'oranges']
# checking_for = ['oranges', 'grapes']
# result = [x not in checking_for for x in original_list]
# print(result)
#
# check = any(x not in checking_for for x in original_list)
#
# print(check)

original_list = ['oranges', 'oranges', 'grapes']
print(original_list)

checking_for = ['oranges', 'grapes']
print(checking_for)
difference = []


def check_if_there_something_else(original_list: list, checking_for: list):
    for fruit in original_list:
        if fruit not in checking_for:
            return True
    return False


# original_list = ['oranges', 'oranges', 'grapes']
# checking_for = ['oranges', 'grapes']
# print(check_if_there_something_else(original_list, checking_for))
# print(any(set(original_list).difference(checking_for)))
#
# original_list = ['oranges', 'oranges', 'grapes', 'grapes', 'grapes', 'kiwi']
# checking_for = ['oranges', 'grapes']
# print(check_if_there_something_else(original_list, checking_for))
# print(any(set(original_list).difference(checking_for)))


original_list = ['oranges', 'oranges', 'grapes', 'grapes', 'grapes', 'kiwi']
checking_for = ['oranges', 'grapes']
print(check_if_there_something_else(original_list, checking_for))
print(any(set(original_list).difference(checking_for)))