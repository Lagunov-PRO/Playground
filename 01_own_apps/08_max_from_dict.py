stats = {'a': 1000, 'b': 3000, 'c': 100, 'd': 3000}
#  Getting the max of all the values
max_value = max(stats.values())
max_stats = []
for key, value in stats.items():
    #  If key has the max value, append it to the list of keys
    if value == max_value:
        max_stats.append(key)
# print(max_stats)

# print(list(stats.items()))


max_key = max(stats, key=lambda k: stats[k])

# print(max_key)


stats = {'a': 1000, 'b': 3000, 'c': 100, 'd': 3000}
max_value = max(stats.values())
for key in stats.keys():
    if stats[key] == max_value:
        break
print(key)

# def find_max_in_dict(your_dict, )
stats = {'a': 1000, 'b': 3000, 'c': 100, 'd': 3000}
max_value = max(stats.values())
max_stats_keys = []
for key in stats.keys():
    if stats[key] == max_value:
        max_stats_keys.append(key)
print(max_stats_keys)


stats = {'a': 1000, 'b': 3000, 'c': 100, 'd': 3000}
max_stats_keys = [key for key in stats if stats[key] == max(stats.values())]
print(max_stats_keys)

max_stats_keys = []
for key in stats:
    if stats[key] == max(stats.values()):
        max_stats_keys.append(key)
print(max_stats_keys)

print(len(stats))
