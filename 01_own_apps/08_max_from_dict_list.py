stats = {'a': [1000, 3000], 'b': [3000, 100], 'c': [100, 5], 'd': [3000]}
#  Flattening the list and getting the max value
# all_values = []
# for value in stats.values():
#     all_values.extend(value)
# max_value = max(all_values)

max_value = 0
for value in stats.values():
    if max(value) > max_value:
        max_value = max(value)

max_stats = []
for key, value in stats.items():
    if max(value) == max_value:
        max_stats.append(key)
print(max_stats)





#  Надяться на порядок в словаре — плохой тон
