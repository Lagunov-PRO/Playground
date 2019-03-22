def sort_by_frequency(elements: list):
    freq = {}
    uniq = set(elements)  # оставляем только уникальные
    for u in uniq:
        freq[u] = elements.count(u)  # пишем количествор в словарь
    result = []
    for x in range(len(freq)):
        for key in freq:
            if freq[key] == max(freq.values()) and max(freq.values()) != 0:
                result.append(key)
                freq[key] = 0
    return result


stats = [1]

f = sort_by_frequency(stats)
print(f)
