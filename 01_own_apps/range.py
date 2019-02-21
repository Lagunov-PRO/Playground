from own_apps.months import list_of_months

print(list_of_months(3))

months = [((month % 12) + 1) for month in range(2, 14)]

print(months)
